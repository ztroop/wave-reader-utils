import asyncio

from wave_reader import discover_wave_devices, fetch_readings_from_devices


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    devices = loop.run_until_complete(discover_wave_devices())
    loop.run_until_complete(fetch_readings_from_devices(devices))
    for d in devices:
        print(str(d.sensors))
