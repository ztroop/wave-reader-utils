# Introduction

![Build Status](https://github.com/ztroop/wave-reader/workflows/Build%20Status/badge.svg)
[![codecov](https://codecov.io/gh/ztroop/wave-reader-utils/branch/master/graph/badge.svg?token=NG9H8YO1ID)](https://codecov.io/gh/ztroop/wave-reader-utils)
[![PyPI version](https://badge.fury.io/py/wave-reader.svg)](https://badge.fury.io/py/wave-reader)
[![Join the chat at https://gitter.im/wave-reader-utils/community](https://badges.gitter.im/wave-reader-utils/community.svg)](https://gitter.im/wave-reader-utils/community?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

This is an **unofficial** Airthings Wave library designed to provide tools and information
around device communication. The library wouldn't be possible without the existing scripts
available by Airthings and contribution of others.

This library uses `bleak` as a dependency instead of `bluepy` for platform cross-compatibility
and support for asynchronous operation.

## Requirements

In Ubuntu Linux, make sure you have `libglib2.0-dev` and `bluez` installed:

```
sudo apt-get install libglib2.0-dev bluez -y
```

In theory, other platforms (Windows, Mac) _are_ supported by using `bleak` as a dependency, but open a ticket if you run into any issues.

## Installation

You can install the library by running:

```sh
pip install wave-reader
```

## Example Usage

There are various concrete examples available in the `examples` directory. This includes
CLI interaction and other scnearios that demonstrate API usage.

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
        sensor_readings = loop.run_until_complete(device.get_sensor_values())
        print(sensor_readings)

# >>> DeviceSensors (humidity: 32.5, radon_sta: 116, radon_lta: 113 ...
```

## Testing

You can run the entire test suite by running `tox`. It will run `flake8`, `isort` and `pytest`.
If you'd like to just run unit tests, running `pytest ./tests` is sufficient.
