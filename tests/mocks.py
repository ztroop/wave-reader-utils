class MockedBLEDevice:
    def __init__(self):
        self.name = "Airthings Wave+"
        self.rssi = -69
        self.metadata = {
            "uuids": [
                "00001800-0000-1000-8000-00805f9b34fb"
                "00001801-0000-1000-8000-00805f9b34fb"
                "0000180a-0000-1000-8000-00805f9b34fb"
                "b42e1c08-ade7-11e4-89d3-123b93f75cba"
                "f000ffc0-0451-4000-b000-000000000000"
            ],
            # Represents '2930618893', a valid serial for a model 2930 (Wave+)
            "manufacturer_data": {820: [13, 178, 173, 174, 9, 0]},
        }
        self.address = "80:XO:XO:XO:EE:48"


class MockedBleakClient(object):
    def __init__(self, addr):
        self.addr = addr
        self.is_connected = False

    async def read_gatt_char(self, _uuid):
        return bytearray(
            b"\x01A\x00\x00\x88\x00\x8f\x00\x0f\x08X\xbf\xb4\x02r\x00\x00\x00\x1c\x06"
        )

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
