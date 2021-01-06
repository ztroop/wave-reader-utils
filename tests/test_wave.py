from copy import deepcopy
from unittest import IsolatedAsyncioTestCase
from unittest.mock import patch

from wave_reader import wave

from .mocks import MockedBleakClient, MockedBLEDevice


class TestWave(IsolatedAsyncioTestCase):
    def setUp(self):
        # A device that is a valid Wave profile.
        self.BLEDevice = MockedBLEDevice()
        self.WaveDevice = wave.WaveDevice(self.BLEDevice, 2862618893)
        self.DeviceSensors = wave.DeviceSensors.from_bytes(
            (1, 65, 0, 0, 136, 143, 2063, 48984, 692, 114, 0, 1564), self.WaveDevice.name
        )

    @patch("wave_reader.wave.discover")
    async def test_discover_wave_devices(self, mocked_discover):
        # A device that should raise an UnknownDevice exception.
        BLEUnknownDevice = deepcopy(self.BLEDevice)
        BLEUnknownDevice.metadata["manufacturer_data"] = {420: [69]}
        # A device that should be ignored because it lacks manu_data.
        BLEIgnoredDevice = deepcopy(self.BLEDevice)
        BLEIgnoredDevice.metadata["manufacturer_data"] = {}

        mocked_discover.return_value = [self.BLEDevice, BLEUnknownDevice, BLEIgnoredDevice]
        expected_result = [self.WaveDevice]
        devices = await wave.discover_wave_devices()
        self.assertTrue((devices == expected_result))

    def test_wave_device__str__(self):
        self.assertEqual(str(self.WaveDevice), 'WaveDevice (2862618893)')

    @patch("wave_reader.wave.BleakClient", autospec=True)
    async def test_fetch_readings_from_devices(self, mocked_client):
        device = [self.WaveDevice]
        mocked_client.return_value = MockedBleakClient(device[0])
        await wave.fetch_readings_from_devices([self.WaveDevice])
        self.assertEqual(device[0].sensors, self.DeviceSensors)

    def test_sensors__str__(self):
        self.assertEqual(
            str(self.DeviceSensors),
            'DeviceSensors (humidity: 32.5, radon_sta: 136, radon_lta: 143, '
            'temperature: 20.63, pressure: 979.68, co2: 692.0, voc: 114.0)'
        )
