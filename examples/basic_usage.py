import asyncio

from wave_reader import discover_devices

if __name__ == "__main__":
    # Event loop to run asynchronous tasks.
    loop = asyncio.get_event_loop()
    # Scan for BTLE Wave devices.
    devices = loop.run_until_complete(discover_devices())
    # Get sensor readings from available wave devices.
    for device in devices:
        print(device.address, device.serial)
        sensor_readings = loop.run_until_complete(device.get_sensor_values())
        print(sensor_readings)

# Example usage:
#
# python basic_usage.py
#
# 12:34:56:78:90:AB 2930123456
# DeviceSensors (humidity: 32.5, radon_sta: 116, radon_lta: 113 ...
