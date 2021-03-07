import argparse
import asyncio
import logging
from typing import Any

from rich.console import Console
from rich.table import Table

from wave_reader import WaveDevice

logging.basicConfig(level=logging.INFO)


def data_table(data: dict, serial: int) -> Table:
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("SERIAL", style="dim", width=12)
    column_data = []
    for k, v in data.items():
        table.add_column(str(k).upper())
        column_data.append(str(v))
    table.add_row(str(serial), *column_data)
    return table


def simple_table(title: str, data: Any):
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column(title, style="dim", width=64)
    table.add_row(data)
    return table


async def run(args):
    console = Console()

    async with WaveDevice.create(args.address, args.serial) as conn:
        if args.characteristic:
            c = await conn.read_gatt_char(args.characteristic)
            console.print(simple_table("Characteristic", c.hex(" ")))
        elif args.descriptor:
            c = await conn.read_gatt_descriptor(args.descriptor)
            console.print(simple_table("Descriptor", c.hex(" ")))
        else:
            await conn.get_sensor_values()
            console.print(data_table(conn.sensor_readings.as_dict(), conn.serial))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Wave sensor readings")
    parser.add_argument("-a", "--address", help="Device address", required=True)
    parser.add_argument("-s", "--serial", help="Device serial number", required=True)
    parser.add_argument("-c", "--characteristic", help="Get characteristic")
    parser.add_argument("-d", "--descriptor", help="Get descriptor")

    args = parser.parse_args()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run(args))


# Example usage:
#
# python cli_usage.py -a "12:34:56:78:90:AB" -s "2930123456"
#
# ┏━━━━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━┳━━━━━━┓
# ┃ SERIAL       ┃ HUMIDITY ┃ RADON_STA ┃ RADON_LTA ┃ TEMPERATURE ┃ PRESSURE ┃ CO2   ┃ VOC  ┃
# ┡━━━━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━╇━━━━━━┩
# │ 2930123456   │ 26.0     │ 128       │ 115       │ 20.74       │ 987.66   │ 647.0 │ 72.0 │
# └──────────────┴──────────┴───────────┴───────────┴─────────────┴──────────┴───────┴──────┘
