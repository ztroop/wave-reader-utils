from copy import deepcopy
from unittest import IsolatedAsyncioTestCase, TestCase
from unittest.mock import MagicMock, patch

from wave_reader import data, wave

from .mocks import MockedBleakClient, MockedBLEDevice


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
    @patch("wave_reader.wave.discover")
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
    @patch("wave_reader.wave.discover")
    async def test_unsupported_discover_devices(self, mocked_discover, mocked_logger):
        """Test device discovery, emit a warning for a detected, but unsupported
        Wave device."""

        BLEUnsupportedDevice = deepcopy(self.BLEDevice)
        # manufacturer data represents serial '2862618893', indicating invalid model '2862'
        BLEUnsupportedDevice.metadata["manufacturer_data"] = {
            820: [13, 25, 160, 170, 9, 0]
        }

        mocked_discover.return_value = [BLEUnsupportedDevice]
        devices = await wave.discover_devices()
        self.assertFalse(devices)
        self.assertTrue(mocked_logger.called)

    @patch("wave_reader.wave.discover")
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
    async def test_get_sensor_values(self, mocked_client):
        """Test ``get_sensor_values`` is functioning correctly."""

        device = [self.WaveDevice]
        device_sensors = wave.DeviceSensors.from_bytes(
            (1, 65, 0, 0, 136, 143, 2063, 48984, 692, 114, 0, 1564),
            self.WaveDevice.product,
        )

        mocked_client.return_value = MockedBleakClient(device[0])
        await device[0].get_sensor_values()
        self.assertEqual(device[0].sensor_readings, device_sensors)

    def test_create_valid_product(self):
        """Test WaveDevice is successfully created using the ``create()`` method."""

        device = wave.WaveDevice.create("12:34:56:78:90:AB", "2900123456")
        self.assertEqual(device.product, data.WaveProduct.WAVE)
        self.assertEqual(device.address, "12:34:56:78:90:AB")
        self.assertEqual(device.serial, "2900123456")

    def test_create_invalid_product(self):
        """Test ValueError exception is raised when a unsupported product is specified."""

        with self.assertRaises(ValueError):
            wave.WaveDevice.create("12:34:56:78:90:AB", "123")

    @patch("wave_reader.wave._logger.error")
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
                "dew_point": 18.44,
                "radon_lta": 115,
                "radon_sta": 125,
            },
        )

        # Wave (Second Gen)
        device = wave.WaveDevice.create("12:34:56:78:90:AB", "2950618893")
        mapped = device._map_sensor_values(
            b"\x01d\x00\x00\x87\x00\x91\x00\xe8\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
        )  # (1, 100, 0, 0, 135, 145, 1000, 0, 0, 0, 0, 0)
        self.assertTrue(mapped)
        self.assertEqual(
            device.sensor_readings.as_dict(),
            {
                "dew_point": 0.04,
                "humidity": 50.0,
                "radon_lta": 145,
                "radon_sta": 135,
                "temperature": 10.0,
            },
        )

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
                "dew_point": 3.56,
            },
        )

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
                "dew_point": 4.25,
            },
        )


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
            "temperature: 20.63, pressure: 979.68, co2: 692.0, voc: 114.0, "
            "dew_point: 3.56)",
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
            "dew_point": 12.62,
        }
        self.assertEqual(device_sensors.as_dict(), expected_dict)

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
            "dew_point": 3.56,
        }
        self.assertEqual(device_sensors.as_dict(), expected_dict)

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
            "dew_point": 10.96,
        }
        self.assertEqual(device_sensors.as_dict(), expected_dict)


class TestRetry(TestCase):
    def test_retry_eventually_successful(self):
        mock = MagicMock(side_effect=(ValueError, ValueError, 100))

        @wave.retry(ValueError, delay=0)
        def fake_function():
            v = mock()
            return v

        r = fake_function()
        self.assertEqual(r, 100)

    def test_retry_failed(self):
        mock = MagicMock(side_effect=(ValueError))

        @wave.retry(ValueError, retries=1, delay=0)
        def fake_function():
            v = mock()
            return v

        with self.assertRaises(ValueError):
            fake_function()
