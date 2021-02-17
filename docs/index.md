# Wave Reader Utils

This is a community-driven project to provide development tools and resources for the Airthings Wave devices. This wouldn't be possible without the contribution of others.

The `wave-reader` library uses `bleak` as a dependency instead of `bluepy` for platform cross-compatibility and support for asynchronous operation.

## Requirements

In Ubuntu Linux, make sure you have `libglib2.0-dev` and `bluez` installed:

```sh
sudo apt-get install libglib2.0-dev bluez -y
```

In theory, other platforms (Windows, Mac) are supported by using bleak as a dependency, but open a ticket if you run into any issues.

## Installation

You can install the library by running:

```sh
pip install wave-reader
```

## Example

```python
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
```
