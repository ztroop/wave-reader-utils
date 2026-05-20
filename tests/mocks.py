class MockedAdvertisementData:
    def __init__(self, manufacturer_data=None):
        self.manufacturer_data = (
            manufacturer_data if manufacturer_data is not None else {}
        )


class MockedBLEDevice:
    def __init__(self):
        self.name = "Airthings Wave+"
        self.rssi = -69
        self.address = "80:XO:XO:XO:EE:48"


class MockedBleakClient(object):
    def __init__(self, addr, battery_response=None):
        self.addr = addr
        self.is_connected = False
        self._battery_response = battery_response
        self._notify_handlers = {}

    async def read_gatt_char(self, _uuid):
        return bytearray(
            b"\x01A\x00\x00\x88\x00\x8f\x00\x0f\x08X\xbf\xb4\x02r\x00\x00\x00\x1c\x06"
        )

    async def start_notify(self, uuid, handler):
        self._notify_handlers[str(uuid)] = handler

    async def stop_notify(self, uuid):
        self._notify_handlers.pop(str(uuid), None)

    async def write_gatt_char(self, uuid, data, response=False):
        handler = self._notify_handlers.get(str(uuid))
        if handler and self._battery_response is not None:
            handler(None, self._battery_response)

    async def connect(self):
        self.is_connected = True
        return True

    async def disconnect(self):
        self.is_connected = False
        return True

    async def __aenter__(self):
        await self.connect()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.disconnect()
        return True


class MockedFailingBleakClient(MockedBleakClient):
    async def connect(self):
        self.is_connected = False
        return False
