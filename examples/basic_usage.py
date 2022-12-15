import asyncio
import logging
from wave_reader.wave import WaveDevice

from wave_reader import discover_devices

logging.basicConfig(level=logging.DEBUG)


async def get_readings(device: WaveDevice) -> None:
    print(device.address, device.serial)
    sensor_readings = await device.get_sensor_values()
    print(sensor_readings)
    await device.disconnect()

if __name__ == "__main__":
    # Event loop to run asynchronous tasks.
    loop = asyncio.get_event_loop()
    # Scan for BTLE Wave devices.
    devices = loop.run_until_complete(discover_devices(timeout=5.0))
    # Get sensor readings from available wave devices.
    for device in devices:
        loop.run_until_complete(get_readings(device))

# Example usage:
#
# python basic_usage.py
#
# 12:34:56:78:90:AB 2930123456
# DeviceSensors (humidity: 32.5, radon_sta: 116, radon_lta: 113 ...
