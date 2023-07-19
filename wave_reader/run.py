import asyncio
import logging

from wave_reader import discover_devices, wave

logging.basicConfig(level=logging.INFO)


async def get_readings(device: wave.WaveDevice) -> None:
    sensor_readings = await device.get_sensor_values()
    print(sensor_readings)
    await device.disconnect()


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    devices = loop.run_until_complete(discover_devices(timeout=5.0))
    for device in devices:
        loop.run_until_complete(get_readings(device))
