import asyncio
import os
from collections import deque
from datetime import datetime

from flask import Flask

from wave_reader import WaveDevice


class RingBuffer(deque):
    def __init__(self, size):
        deque.__init__(self)
        self.size = size

    def full_append(self, item):
        deque.append(self, item)
        self.popleft()

    def append(self, item):
        deque.append(self, item)
        if len(self) == self.size:
            self.append = self.full_append

    def get(self):
        return list(self)


loop = asyncio.get_event_loop()
app = Flask(__name__)
device = WaveDevice.create(
    os.environ["WAVE_PRODUCT"], os.environ["WAVE_ADDRESS"], os.environ["WAVE_SERIAL"]
)
ring_buffer = RingBuffer(8760)


async def get_sensor_readings():
    values = await device.get_sensor_values()
    ring_buffer.append(tuple(datetime.utcnow, values.as_dict()))


loop.call_later(3600, get_sensor_readings)


@app.route("/")
def show_all_readings():
    return ring_buffer, 200


if __name__ == "__main__":
    app.run(debug=False, use_reloader=False)
