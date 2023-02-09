import argparse
import asyncio
import logging

from wave_reader.wave import WaveDevice

logging.basicConfig(level=logging.INFO)


async def run(args):
    async with WaveDevice.create(args.address, args.serial) as conn:
        services = await conn.get_services()
        for handle, service in services.items():
            print(f"Service: {service.uuid} (Handle: {handle})")
            for characteristic in service.characteristics:
                print(f"- Characteristic: {characteristic.uuid}")
                print(f"-- Flag: {characteristic.properties}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Wave sensor readings")
    parser.add_argument("-a", "--address", help="Device address", required=True)
    parser.add_argument("-s", "--serial", help="Device serial number", required=True)

    args = parser.parse_args()
    loop = asyncio.new_event_loop()
    loop.run_until_complete(run(args))
