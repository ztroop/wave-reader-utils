![Build Status](https://github.com/ztroop/wave-reader/workflows/Build%20Status/badge.svg)
[![codecov](https://codecov.io/gh/ztroop/wave-reader-utils/branch/master/graph/badge.svg?token=NG9H8YO1ID)](https://codecov.io/gh/ztroop/wave-reader-utils)
[![PyPI version](https://badge.fury.io/py/wave-reader.svg)](https://badge.fury.io/py/wave-reader)
[![PyPI downloads](https://img.shields.io/pypi/dm/wave-reader)](https://pypi.org/project/wave-reader/)

## Wave Reader Utilities

The `Airthings Wave` is a series of devices that track Radon levels in the home. Radon is a radioactive
gas that comes from the breakdown of uranium in soil and rock. It's invisible, odourless and tasteless.

This is an **unofficial** Airthings Wave community library designed to provide utilities for device
and web communication. The library wouldn't be possible without the existing efforts from Airthings
and the community. See [documentation](https://ztroop.github.io/wave-reader-utils/) for more information.

## Features

- Using `bleak` as a dependency for platform cross-compatibility and support for asynchronous operation.
- Support for major models: Wave+, Wave, Wave (Version 2) and Wave Mini devices. View Plus is not supported, as it sends data over WiFi, not BTLE.
- Code testing, coverage reporting, linting, type hinting, and formatting.
- Provide a more comprehensive programming interface for a developer audience.
- Auxillary module that provides a web client for Airthings API and OAuth2 authentication.

## Requirements

In Ubuntu/Debian, make sure you have `libglib2.0-dev` and `bluez` installed:

```sh
sudo apt-get install libglib2.0-dev bluez -y
```

Other Linux distributions should have equivalent packages. In theory, other platforms
(Windows, Mac) _are_ supported by using `bleak` as a dependency, but open a ticket
if you run into any issues.

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
    loop = asyncio.new_event_loop()
    # Get sensor readings from available wave devices.
    for d in devices:
        sensor_readings = loop.run_until_complete(d.get_sensor_values())
        print(sensor_readings)

# >>> DeviceSensors (humidity: 32.5, radon_sta: 116, radon_lta: 113 ...
```

## Web API Client Module

The `wave_reader/web` module in this library provides a client for the Airthings
web API. See [this page](./wave_reader/web/README.md) for more details.

## Contribution

If you identify a bug, please open a ticket. Pull requests are always welcome.

## Testing

You can run the entire test suite by running `tox`. It will run `flake8`, `isort` and `pytest`.
If you'd like to just run unit tests, running `pytest ./tests` is sufficient.
