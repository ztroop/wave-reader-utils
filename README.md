![Build Status](https://github.com/ztroop/wave-reader/workflows/Build%20Status/badge.svg)
[![codecov](https://codecov.io/gh/ztroop/wave-reader/branch/master/graph/badge.svg?token=NG9H8YO1ID)](https://codecov.io/gh/ztroop/wave-reader)
[![PyPI version](https://badge.fury.io/py/wave-reader.svg)](https://badge.fury.io/py/wave-reader)

## Summary

This is an **unofficial** Airthings Wave library designed to provide software developers
a more developer-friendly library for BTLE handling for Airthings Wave devices.
This library wouldn't be possible without the documentation and scripts available
by Airthings. I hope to continue making updates through Airthings continued
open-source contributions.

This library uses `bleak` as a dependency instead of `bluepy` for platform
cross-compatibility and support for asynchronous operation.

This project is currently in **alpha** state.

## Goals

These are the goals for this project, _in no particular order_:

- [x] Support platform cross-compatibility. Windows, Mac and Linux.
- [x] Support WavePlus, Wave (Version 2) and Wave Mini devices.
- [x] Support operation across multiple devices asynchronously.
- [x] Code testing, linting, type hinting, formatting and coverage reporting.
- [x] Discover all Wave devices or inherit WaveDevice class for sensor readings.
- [ ] Add battery life support.
- [ ] Implement reconnection logic for BTLE client.
- [ ] Support other devices like Wave (Version 1) and more.

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

## Special Thanks

I'd like to thank Airthings for their open-source work and commitment to air quality.
Radon and other air pollutants often go unnoticed, so knowledge (really) is power here.
