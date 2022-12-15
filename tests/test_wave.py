from copy import deepcopy
from unittest import IsolatedAsyncioTestCase, TestCase
from unittest.mock import patch

from wave_reader import data, wave
from wave_reader.utils import requires_client

from .mocks import MockedBleakClient, MockedBLEDevice, MockedFailingBleakClient


class TestReaderUtils(TestCase):
    def test_parse_manufacturer_data(self):
        """Test manufacturer data parsing."""

        valid_data = {820: [13, 25, 160, 170, 9, 0]}
        valid_serial = wave.WaveDevice.parse_manufacturer_data(valid_data)
        self.assertEqual(valid_serial, "2862618893")
        # Test examples of invalid data.
        invalid_data = [
            {},
            None,
            {120: []},
            {120: None},
            {820: [10, 20]},
            {120: [13, 25, 160, 170, 9, 0]},
        ]
        for i in invalid_data:
            self.assertFalse(wave.WaveDevice.parse_manufacturer_data(i))


class TestWaveDevice(IsolatedAsyncioTestCase):
    def setUp(self):
        self.BLEDevice = MockedBLEDevice()
        self.WaveDevice = wave.WaveDevice(self.BLEDevice, "2930618893")

    @patch("wave_reader.wave._logger.debug")
    @patch("wave_reader.wave.BleakScanner.discover")
    async def test_discover_devices(self, mocked_discover, mocked_logger):
        """Test device discovery, omitting invalid or unknown devices."""

        # A device that should raise an UnknownDevice exception.
        BLEUnknownDevice = deepcopy(self.BLEDevice)
        BLEUnknownDevice.metadata["manufacturer_data"] = {420: [69]}
        # A device that should be ignored because it lacks manu_data.
        BLEIgnoredDevice = deepcopy(self.BLEDevice)
        BLEIgnoredDevice.metadata["manufacturer_data"] = {}

        mocked_discover.return_value = [
            self.BLEDevice,
            BLEUnknownDevice,
            BLEIgnoredDevice,
        ]
        expected_result = [self.WaveDevice]
        devices = await wave.discover_devices()
        self.assertTrue((devices == expected_result))
        self.assertTrue(mocked_logger.called)

    @patch("wave_reader.wave._logger.warning")
    @patch("wave_reader.wave.BleakScanner.discover")
    async def test_unsupported_discover_devices(self, mocked_discover, mocked_logger):
        """Test device discovery, emit a warning for a detected, but unsupported
        Wave device."""

        BLEUnsupportedDevice = deepcopy(self.BLEDevice)
        # Manufacturer data represents serial '2862618893', indicating invalid model '286'
        BLEUnsupportedDevice.metadata["manufacturer_data"] = {
            820: [13, 25, 160, 170, 9, 0]
        }

        mocked_discover.return_value = [BLEUnsupportedDevice]
        devices = await wave.discover_devices()
        self.assertEqual(devices[0].product, data.WaveProduct.UNKNOWN)
        self.assertTrue(mocked_logger.called)

    @patch("wave_reader.wave.BleakScanner.discover")
    async def test_discover_valid_unnamed_device(self, mocked_discover):
        """Test device discovery when the BLE advertisement does not include the model name."""
        BLEUnnamedDevice = deepcopy(self.BLEDevice)
        BLEUnnamedDevice.name = BLEUnnamedDevice.address.replace(":", "-")

        mocked_discover.return_value = [BLEUnnamedDevice]
        devices = await wave.discover_devices()
        self.assertNotEqual(devices, [])

    def test_wave_device__str__(self):
        """Test the __str__ method is matching our expected value."""

        self.assertEqual(str(self.WaveDevice), "WaveDevice (2930618893)")

    def test_wavedevice__eq__(self):
        """Test the __eq__ method is functioning correctly."""

        wave_device_copy = deepcopy(self.WaveDevice)
        wave_device_modified = deepcopy(self.WaveDevice)
        wave_device_modified.name = "Other Device"
        self.assertTrue(self.WaveDevice == wave_device_copy)
        self.assertFalse(self.WaveDevice == wave_device_modified)

    @patch("wave_reader.wave.BleakClient", autospec=True)
    async def test_context_manager(self, mocked_client):
        device = wave.WaveDevice.create("12:34:56:78:90:AB", "2900123456")
        mocked_client.return_value = MockedBleakClient(device.address)

        async with device as connected_device:
            self.assertEqual(connected_device.address, "12:34:56:78:90:AB")
            self.assertEqual(connected_device.serial, "2900123456")
            self.assertTrue(connected_device._client.is_connected)

    @patch("wave_reader.wave.BleakClient", autospec=True)
    async def test_get_sensor_values(self, mocked_client):
        """Test ``get_sensor_values`` is functioning correctly."""

        device = wave.WaveDevice.create("12:34:56:78:90:AB", "2930123456")
        device_sensors = wave.DeviceSensors.from_bytes(
            (1, 65, 0, 0, 136, 143, 2063, 48984, 692, 114, 0, 1564),
            data.WaveProduct.WAVEPLUS,
        )

        mocked_client.return_value = MockedBleakClient(device.address)
        await device.get_sensor_values()
        self.assertEqual(device.sensor_readings, device_sensors)

    def test_create_valid_product(self):
        """Test WaveDevice is successfully created using the ``create()`` method."""

        device = wave.WaveDevice.create("12:34:56:78:90:AB", "2900123456")
        self.assertEqual(device.product, data.WaveProduct.WAVE)
        self.assertEqual(device.address, "12:34:56:78:90:AB")
        self.assertEqual(device.serial, "2900123456")

    @patch("wave_reader.wave._logger.warning")
    def test_create_invalid_product(self, mocked_logger):
        """Test warning is sent when a unsupported product is specified."""

        wave.WaveDevice.create("12:34:56:78:90:AB", "123")
        self.assertTrue(mocked_logger.called)

    @patch("wave_reader.utils._logger.error")
    def test_invalid_map_sensor_values(self, mocked_logger):
        """Test errors around binary data handling."""

        device = wave.WaveDevice.create("12:34:56:78:90:AB", "2900123456")
        with self.assertRaises(wave.UnsupportedError):
            device._map_sensor_values(b"\x01A\x00\x00")
        self.assertTrue(mocked_logger.called)

        device = wave.WaveDevice.create("12:34:56:78:90:AB", "2930123456")
        with self.assertRaises(wave.UnsupportedError):
            device._map_sensor_values(
                b"\x02A\x00\x00\x88\x00\x8f\x00\x0f\x08X\xbf\xb4\x02r\x00\x00\x00\x1c\x06"
            )
        self.assertTrue(mocked_logger.called)

    def test_valid_map_sensor_values(self):
        """Test binary data examples for each Wave device."""

        # Wave (First Gen)
        device = wave.WaveDevice.create("12:34:56:78:90:AB", "2900123456")
        mapped = device._map_sensor_values(
            b"\x00\x00\x00\x00\x00\x00\x00\x88\x13\xb8\x0b}\x00s\x00"
        )  # (0, 0, 0, 0, 0, 0, 5000, 3000, 125, 115)
        self.assertTrue(mapped)
        self.assertEqual(
            device.sensor_readings.as_dict(),
            {
                "humidity": 50.0,
                "temperature": 30.0,
                "radon_lta": 115,
                "radon_sta": 125,
            },
        )
        self.assertEqual(device.sensor_readings.dew_point, 18.44)

        # Wave (Second Gen)
        device = wave.WaveDevice.create("12:34:56:78:90:AB", "2950618893")
        mapped = device._map_sensor_values(
            b"\x01d\x00\x00\x87\x00\x91\x00\xe8\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
        )  # (1, 100, 0, 0, 135, 145, 1000, 0, 0, 0, 0, 0)
        self.assertTrue(mapped)
        self.assertEqual(
            device.sensor_readings.as_dict(),
            {
                "humidity": 50.0,
                "radon_lta": 145,
                "radon_sta": 135,
                "temperature": 10.0,
            },
        )
        self.assertEqual(device.sensor_readings.dew_point, 0.04)

        # Wave Plus
        device = wave.WaveDevice.create("12:34:56:78:90:AB", "2930618893")
        mapped = device._map_sensor_values(
            b"\x01A\x00\x00\x88\x00\x8f\x00\x0f\x08X\xbf\xb4\x02r\x00\x00\x00\x1c\x06"
        )  # (1, 65, 0, 0, 136, 143, 2063, 48984, 692, 114, 0, 1564)
        self.assertTrue(mapped)
        self.assertEqual(
            device.sensor_readings.as_dict(),
            {
                "co2": 692.0,
                "humidity": 32.5,
                "pressure": 979.68,
                "radon_lta": 143,
                "radon_sta": 136,
                "temperature": 20.63,
                "voc": 114.0,
            },
        )
        self.assertEqual(device.sensor_readings.dew_point, 3.56)

        # Wave Mini
        device = wave.WaveDevice.create("12:34:56:78:90:AB", "2920618893")
        mapped = device._map_sensor_values(
            b"\x01\x00\x94s\x00\x00\xb8\x0b\xc8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
        )  # (1, 29588, 0, 3000, 200, 0, 0, 0)
        self.assertTrue(mapped)
        self.assertEqual(
            device.sensor_readings.as_dict(),
            {
                "voc": 200,
                "humidity": 30.0,
                "temperature": 22.73,
            },
        )
        self.assertEqual(device.sensor_readings.dew_point, 4.25)


class TestScan(TestCase):
    def setUp(self) -> None:
        self.BLEDevice = MockedBLEDevice()
        self.WaveDevice = wave.WaveDevice(self.BLEDevice, "2930618893")

    @patch("wave_reader.wave.BleakScanner.discover")
    def test_scan(self, mocked_discover):
        mocked_discover.return_value = [self.WaveDevice]

        devices = wave.scan()
        self.assertEqual(devices, [self.WaveDevice])

    @patch("wave_reader.wave._logger.warning")
    @patch("wave_reader.wave._logger.error")
    @patch("wave_reader.wave.asyncio.new_event_loop")
    def test_failing_scan(self, mocked_discover, mocked_log_err, mocked_log_warn):
        # We're trying to catch upstream failures. For example, bleak might raise
        # a txdbus.error.RemoteError or related exception (bleak.exc.BleakError)
        # potentially due to txdbus and how it handles the DBus connections.
        #
        # See Issue #5 for more information.
        mocked_discover.side_effect = Exception()
        devices = wave.scan()

        self.assertEqual(len(mocked_log_warn.mock_calls), 3)
        mocked_log_err.assert_called_once()
        self.assertEqual(devices, [])


class TestDeviceSensors(TestCase):
    """TestCase for DeviceSensors class."""

    def test_sensors__str__(self):
        """Test the __str__ method is matching our expected value."""

        self.assertEqual(
            str(
                wave.DeviceSensors.from_bytes(
                    (1, 65, 0, 0, 136, 143, 2063, 48984, 692, 114, 0, 1564),
                    data.WaveProduct.WAVEPLUS,
                )
            ),
            "DeviceSensors (humidity: 32.5, radon_sta: 136, radon_lta: 143, "
            "temperature: 20.63, pressure: 979.68, co2: 692.0, voc: 114.0)",
        )

    def test_as_tuple(self):
        fields = wave.DeviceSensors.from_bytes(
            (1, 125, 0, 0, 140, 145, 2000),
            data.WaveProduct.WAVE2,
        ).as_tuple()
        self.assertTrue(isinstance(fields, tuple))
        self.assertEqual(len(fields), 8)

    def test_wave2(self):
        """Test WAVE2 device is returning the correct sensor values."""

        device_sensors = wave.DeviceSensors.from_bytes(
            (1, 125, 0, 0, 140, 145, 2000),
            data.WaveProduct.WAVE2,
        )
        expected_dict = {
            "humidity": 62.5,
            "radon_lta": 145,
            "radon_sta": 140,
            "temperature": 20.0,
        }
        self.assertEqual(device_sensors.as_dict(), expected_dict)
        self.assertEqual(device_sensors.dew_point, 12.62)

    def test_wave_plus(self):
        """Test WAVEPLUS device is returning the correct sensor values."""

        device_sensors = wave.DeviceSensors.from_bytes(
            (1, 65, 0, 0, 136, 143, 2063, 48984, 692, 114, 0, 1564),
            data.WaveProduct.WAVEPLUS,
        )
        expected_dict = {
            "humidity": 32.5,
            "radon_sta": 136,
            "radon_lta": 143,
            "temperature": 20.63,
            "pressure": 979.68,
            "co2": 692.0,
            "voc": 114.0,
        }
        self.assertEqual(device_sensors.as_dict(), expected_dict)
        self.assertEqual(device_sensors.dew_point, 3.56)

    def test_wave_mini(self):
        """Test WAVEMINI device is returning the correct sensor values."""

        device_sensors = wave.DeviceSensors.from_bytes(
            (1, 29500, 0, 5000, 600),
            data.WaveProduct.WAVEMINI,
        )
        expected_dict = {
            "humidity": 50.0,
            "temperature": 21.85,
            "voc": 600,
        }
        self.assertEqual(device_sensors.as_dict(), expected_dict)
        self.assertEqual(device_sensors.dew_point, 10.96)


class TestRequiresClient(IsolatedAsyncioTestCase):
    """Test the ``requires_client`` decorator."""

    @patch("wave_reader.utils._logger.error")
    @patch("wave_reader.wave.BleakClient", autospec=True)
    async def test_requires_client(self, mocked_client, mocked_logger):
        device = wave.WaveDevice.create("12:34:56:78:90:AB", "2930123456")
        mocked_client.return_value = MockedBleakClient(device.address)
        device._client = None

        @requires_client
        async def fake_function(d):
            return d.is_connected

        # After not being connected, successfully connect.
        self.assertTrue(await fake_function(device))

        mocked_client.return_value = MockedFailingBleakClient(device.address)
        device._client = None

        # We intentionally fail the connect to show the loop exists after 3 reconnects.
        self.assertFalse(await fake_function(device))
        self.assertEqual(mocked_logger.call_count, 1)
