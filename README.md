## Summary

This is an **unofficial** Airthings Wave library designed to provide software developers
a more developer-friendly library for BTLE handling for Airthings Wave devices.
This library wouldn't be possible without the documentation and scripts available
by Airthings. I hope to continue making updates through Airthing's continued
open-source contributions.

This library uses `bleak` as a dependency instead of `bluepy` for platform
cross-compatibility and support for asynchronous operation.

This project is currently in **alpha** state.

## Goals

These are the goals for this project, _in no particular order_:

- [x] Support platform cross-compatibility. Windows, Mac an Linux.
- [x] Support WavePlus & Wave (Version 2) devices.
- [x] Code testing, linting, type hinting, formatting and coverage reporting.
- [x] Discover all Wave devices or manually construct a WaveDevice for pulling readings.
- [x] Support interaction/operation across multiple Wave devices.
- [ ] Add battery life support.
- [ ] Implement reconnection logic for BTLE client.
- [ ] Support other devices like Wave (Version 1) and Mini.
- [ ] Add other interfaces like MQTT, AMQP and more!

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
from wave_reader import WaveDevice, discover_wave_devices, fetch_readings_from_devices

if __name__ == "__main__":
    # Event loop to run asynchronous tasks.
    loop = asyncio.get_event_loop()
    # Scan for BTLE Wave devices.
    available_wave_devices = loop.run_until_complete(discover_wave_devices())
    # Add/Update sensor readings to the available wave devices.
    loop.run_until_complete(fetch_readings_from_devices(available_wave_devices))
    # You could also construct your own WaveDevice objects if you already
    # know the serial number and other relevant details.
    loop.run_until_complete(
        fetch_readings_from_devices(
            [WaveDevice(...), WaveDevice(...)]
        )
    )
```

## Testing

You can run the entire test suite by running `tox`. It will run `flake8`, `isort` and `pytest`.
If you'd like to just run unit tests, running `pytest ./tests` is sufficient.

## Special Thanks

I'd like to thank Airthings for their open-source work and commitment to air quality.
Radon and other air pollutants often go unnoticed, so knowledge (really) is power here.