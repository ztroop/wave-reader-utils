import logging
from functools import wraps

_logger = logging.getLogger(__name__)


class UnsupportedError(Exception):
    """Custom exception class for unsupported device errors.

    :param message: The error message
    :param name: The device name
    :param addr: The device address (UUID in MacOS, MAC in Linux/Windows)
    """

    def __init__(self, message: str, addr: str):
        self.message = f"Device: ({addr}) -> {message}"
        _logger.error(self.message)
        super().__init__(self.message)


def requires_client(f):
    """Decorator that verifies the existance of the client implementation."""

    @wraps(f)
    async def _requires_client(self, *args, **kwargs):
        reconnects = 0

        while not self._client or not self._client.is_connected:
            await self.connect()

            reconnects += 1
            if reconnects > 3:
                _logger.error(f"Device: ({self.address}) client is not connected.")
                return

        return await f(self, *args, **kwargs)

    return _requires_client


def battery_percentage(voltage: float, battery_count: int = 2) -> int:
    """Calculate battery percentage based on voltage.

    :param voltage: The battery voltage in volts.
    :param battery_count: The number of batteries (2 or 3).
    :return: The estimated battery percentage.
    """

    if battery_count == 3:
        # Wave Mini: 3 batteries (2.4V - 4.5V)
        if voltage >= 4.50:
            return 100
        if voltage >= 4.20:
            return _interpolate(voltage, (4.20, 4.50), (85, 100))
        if voltage >= 3.90:
            return _interpolate(voltage, (3.90, 4.20), (62, 85))
        if voltage >= 3.75:
            return _interpolate(voltage, (3.75, 3.90), (42, 62))
        if voltage >= 3.30:
            return _interpolate(voltage, (3.30, 3.75), (23, 42))
        if voltage >= 2.40:
            return _interpolate(voltage, (2.40, 3.30), (0, 23))
        return 0

    # 2-battery devices (2.1V - 3.0V)
    if voltage >= 3.00:
        return 100
    if voltage >= 2.80:
        return _interpolate(voltage, (2.80, 3.00), (81, 100))
    if voltage >= 2.60:
        return _interpolate(voltage, (2.60, 2.80), (53, 81))
    if voltage >= 2.50:
        return _interpolate(voltage, (2.50, 2.60), (28, 53))
    if voltage >= 2.20:
        return _interpolate(voltage, (2.20, 2.50), (5, 28))
    if voltage >= 2.10:
        return _interpolate(voltage, (2.10, 2.20), (0, 5))
    return 0


def _interpolate(
    voltage: float,
    voltage_range: tuple,
    percentage_range: tuple,
) -> int:
    """Linearly interpolate a percentage from a voltage range."""

    return round(
        (voltage - voltage_range[0])
        / (voltage_range[1] - voltage_range[0])
        * (percentage_range[1] - percentage_range[0])
        + percentage_range[0]
    )
