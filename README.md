![Build Status](https://github.com/ztroop/wave-reader/workflows/Build%20Status/badge.svg)
[![codecov](https://codecov.io/gh/ztroop/wave-reader-utils/branch/master/graph/badge.svg?token=NG9H8YO1ID)](https://codecov.io/gh/ztroop/wave-reader-utils)
[![PyPI version](https://badge.fury.io/py/wave-reader.svg)](https://badge.fury.io/py/wave-reader)
[![PyPI downloads](https://img.shields.io/pypi/dm/wave-reader)](https://pypi.org/project/wave-reader/)

## Summary

This is an **unofficial** Airthings Wave library designed to provide tools and information
around device communication. The library wouldn't be possible without the existing scripts
available by Airthings and contribution of others.
See [documentation](https://ztroop.github.io/wave-reader-utils/) for more information.

This library uses `bleak` as a dependency instead of `bluepy` for platform cross-compatibility
and support for asynchronous operation.

## Goals

These are the goals for this project, _in no particular order_:

- [x] Support platform cross-compatibility. Windows, Mac and Linux.
- [x] Support WavePlus, Wave (Version 2) and Wave Mini devices.
- [x] Support operation across multiple devices asynchronously.
- [x] Code testing, linting, type hinting, formatting and coverage reporting.
- [x] Discover all Wave devices or inherit WaveDevice class for sensor readings.
- [x] Support other devices like Wave (Version 1).
- [ ] Add View Plus support.
- [ ] Add battery life support.

## Requirements

In Ubuntu Linux, make sure you have `libglib2.0-dev` and `bluez` installed:

```sh
sudo apt-get install libglib2.0-dev bluez -y
```

In theory, other platforms (Windows, Mac) _are_ supported by using `bleak` as a dependency, but open a ticket if you run into any issues.

## Installation

You can install the library by running:

```sh
pip install wave-reader
```

## Example Usage

There are various concrete examples available in the `examples` directory. That includes
CLI interaction and other interesting scenarios that demonstrate API usage.

```python
import asyncio
from wave_reader import wave

if __name__ == "__main__":
    # Scan for BTLE Wave devices.
    devices = wave.scan()
    # Event loop to run asynchronous tasks.
    loop = asyncio.get_event_loop()
    # Get sensor readings from available wave devices.
    for d in devices:
        sensor_readings = loop.run_until_complete(d.get_sensor_values())
        print(sensor_readings)

# >>> DeviceSensors (humidity: 32.5, radon_sta: 116, radon_lta: 113 ...
```

## Testing

You can run the entire test suite by running `tox`. It will run `flake8`, `isort` and `pytest`.
If you'd like to just run unit tests, running `pytest ./tests` is sufficient.
