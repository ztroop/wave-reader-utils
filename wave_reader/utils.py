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
