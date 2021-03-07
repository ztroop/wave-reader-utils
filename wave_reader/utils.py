import logging
from functools import wraps
from time import sleep
from typing import Any

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


def retry(exceptions: Any, retries: int, delay: int):
    """Decorator to gracefully handle and retry raised exceptions.

    :param exceptions: The exceptions to catch
    :param retries: The amount of times we will retry before raising
    :param delay: The amount of time in seconds before retrying
    """

    def decorator(f):
        @wraps(f)
        def _retry(*args, **kwargs):
            attempts = 0
            while attempts <= retries:
                attempts += 1
                try:
                    return f(*args, **kwargs)
                except exceptions as err:
                    if attempts >= retries:
                        raise
                    _logger.error(err)
                    sleep(delay)
                    continue

        return _retry

    return decorator


def requires_client(f):
    """Decorator that verifies the existance of the client implementation."""

    @wraps(f)
    async def _requires_client(self, *args, **kwargs):
        reconnects = 0

        while not self._client or not await self._client.is_connected():
            _logger.error(f"Device: ({self.address}) client is not connected.")
            await self.connect()

            reconnects += 1
            if reconnects > 3:
                return

        return await f(self, *args, **kwargs)

    return _requires_client
