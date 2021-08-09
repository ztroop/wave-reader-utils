# API Documentation

<a name="wave_reader.wave.DeviceSensors"></a>
## DeviceSensors Objects

```python
@dataclass
class DeviceSensors()
```

A dataclass to encapsulate sensor data.

**Arguments**:

- `humidity`: Relative humidity level (%rH)
- `radon_sta`: Short-term average for radon level (Bq/m3)
- `radon_lta`: Long-term average for radon level (Bq/m3)
- `temperature`: Ambient temperature (°C)
- `pressure`: Atmospheric pressure (hPa)
- `co2`: Carbon dioxide level (ppm)
- `voc`: Volatile organic compound level (ppb)
- `pm`: Particulate matter (ug/m3)

<a name="wave_reader.wave.DeviceSensors.as_dict"></a>
#### as\_dict

```python
 | as_dict() -> Dict[str, Union[int, float]]
```

Returns a dictionary of populated dataclass fields.

<a name="wave_reader.wave.DeviceSensors.as_tuple"></a>
#### as\_tuple

```python
 | as_tuple() -> tuple
```

Return a tuple of all dataclass fields.

<a name="wave_reader.wave.DeviceSensors.dew_point"></a>
#### dew\_point

```python
 | @property
 | dew_point() -> Optional[float]
```

Dew point approximation using the Magnus formula. (°C)

<a name="wave_reader.wave.DeviceSensors.from_bytes"></a>
#### from\_bytes

```python
 | @classmethod
 | from_bytes(cls, data: List[int], product: WaveProduct)
```

Instantiate the class with raw sensor values and the ``WaveProduct``
selection. Each product can have different sensors or may require the
raw data to be handled differently.

<a name="wave_reader.wave.WaveDevice"></a>
## WaveDevice Objects

```python
class WaveDevice()
```

An object that represents a Airthings Wave device. The
``discover_devices`` returns a list of ``BLEDevice`` objects
that are used in the first parameter.

If you want to instantiate a WaveDevice manually without using
discovery, you can create a generic object with the following
properties: ``name``, ``address`` and optionally ``rssi``, ``metadata``.

**Arguments**:

- `device`: Device information from Bleak's discover function
- `serial`: Parsed serial number from manufacturer data

<a name="wave_reader.wave.WaveDevice.connect"></a>
#### connect

```python
 | async connect() -> bool
```

Method for initiating BLE connection.

<a name="wave_reader.wave.WaveDevice.is_connected"></a>
#### is\_connected

```python
 | @requires_client
 | async is_connected() -> bool
```

Method for determining the status of the BLE connection.

<a name="wave_reader.wave.WaveDevice.disconnect"></a>
#### disconnect

```python
 | @requires_client
 | async disconnect() -> bool
```

Method for closing BLE connection.

<a name="wave_reader.wave.WaveDevice.read_gatt_descriptor"></a>
#### read\_gatt\_descriptor

```python
 | @requires_client
 | async read_gatt_descriptor(gatt_desc: str) -> Optional[bytearray]
```

Read Generic Attribute Profile GATT descriptor data.

**Arguments**:

- `handle`: Specify a descriptor UUID string

<a name="wave_reader.wave.WaveDevice.read_gatt_characteristic"></a>
#### read\_gatt\_characteristic

```python
 | @requires_client
 | async read_gatt_characteristic(gatt_char: str) -> bytearray
```

Read Generic Attribute Profile GATT characteristic data.

**Arguments**:

- `gatt_char`: Specify a characteristic UUID string

<a name="wave_reader.wave.WaveDevice.get_services"></a>
#### get\_services

```python
 | @requires_client
 | async get_services() -> Dict
```

Get available services, descriptors and characteristics for the device.

<a name="wave_reader.wave.WaveDevice.get_sensor_values"></a>
#### get\_sensor\_values

```python
 | @requires_client
 | async get_sensor_values() -> Optional[DeviceSensors]
```

Get sensor values from the specified Wave device.

<a name="wave_reader.wave.WaveDevice.parse_manufacturer_data"></a>
#### parse\_manufacturer\_data

```python
 | @staticmethod
 | parse_manufacturer_data(manufacturer_data: Dict[int, int]) -> Optional[str]
```

Converts manufacturer data and returns a serial number for the
Airthings Wave devices.

**Arguments**:

- `manufacturer_data`: The device manufacturer data

<a name="wave_reader.wave.WaveDevice.create"></a>
#### create

```python
 | @classmethod
 | create(cls, address: str, serial: str)
```

Create a WaveDevice instance with arguments.

**Arguments**:

- `address`: The device UUID in MacOS, or MAC in Linux and Windows.
- `serial`: The serial number for the device.

<a name="wave_reader.wave.discover_devices"></a>
#### discover\_devices

```python
async discover_devices(wave_devices: Optional[List[WaveDevice]] = None) -> List[WaveDevice]
```

Discovers all valid, accessible Airthings Wave devices.

<a name="wave_reader.wave.scan"></a>
#### scan

```python
scan(max_retries: int = 3) -> List[WaveDevice]
```

Convenience function for discovering devices. This is particularly useful
for users that are not as comfortable asynchronous programming.

**Arguments**:

- `max_retries`: Number of attempts for connecting to devices
