# Device Specifications

While Airthings has been kind enough to provide sample code for interfacing with
their Wave family of devices, most of the technical details have to be inferred
from the code or discovered via experimentation. This is an unofficial attempt to
document those specifications, in hopes that they may be useful to other
projects.

## Models

| Model | Product Name   | Serial     | Sensors
| :-----| :----          | :-----     | :------
| 2900  | Wave           | 2900xxxxxx | radon, temperature, humidity
| 2920  | Wave Mini      | 2920xxxxxx | temperature, humidity, TVOCs, CO<sub>2</sub>
| 2930  | Wave Plus      | 2930xxxxxx | radon, temperature, humidity, TVOCs, CO<sub>2</sub>
| 2950  | Wave (2nd gen) | 2950xxxxxx | radon, temperature, humidity

## Bluetooth Low Energy (BLE)

### BLE Advertisement

A standard BLE advertisement contains 4 attributes: `name`, `address`, `rssi`, and `metadata`.

#### BLE Advertisement - Name

The `name` attribute *may* be populated with an Airthings name based on the model.

| Model | BLE Advertised Name
| :-----| :----
| 2900  | Airthings Wave (not verified)
| 2920  | Airthings Wave Mini (not verified)
| 2930  | Airthings Wave+
| 2950  | Airthings Wave2

Advertisements are **not guaranteed** to be populated with this descriptive
name, possibly appearing as a variant of the MAC address (e.g.
`12-34-56-78-90-AD`).

#### BLE Advertisement - Metadata

The standard BLE `metadata` attribute consists of two sub-attributes:

A `uuids` attribute contains the BLE service UUIDs avaialble on the device.
For the Airthings Wave family, this UUID has been seen to be:

- `b42e4a8e-ade7-11e4-89d3-123b93f75cba` (read from a Wave2)

Whether or not this servce UUID varies by device has not been verified.

The `manufacturer_data` attribute contains vendor-specific device data, indexed
by [company ID](https://www.bluetooth.com/specifications/assigned-numbers/company-identifiers/company).
For Airthings devices, this ID is always:

- `820` / `0x0334`

This ID is registered to `Corentium AS`.

The manufacturer data under this ID contains the device serial number. See [Data Formats](#ble-manufacturer-data)

### BLE Services

Wave devices expose multiple BLE services.

| Service UUID                         | Description                      | Notes                       |
| :---                                 | :---                             | :---                        |
| 00001801-0000-1000-8000-00805f9b34fb | Generic Attribute Profile        |                             |
| 0000180a-0000-1000-8000-00805f9b34fb | Device Information               |                             |
| f000ffc0-0451-4000-b000-000000000000 | TI Over-the-Air Download Service | Likely Firmware Related     |
| b42e4a8e-ade7-11e4-89d3-123b93f75cba | Airthings                        | Wave2 only                  |
| b42e1c08-ade7-11e4-89d3-123b93f75cba | Airthings                        | Wave+ only                  |

### BLE Characteristics

#### Standard BLE Device Information

| Characteristic UUID                  | Actions | Name                     | Value / Example               |
| :---                                 | :---    | :---                     | :---                          |
| 00002a29-0000-1000-8000-00805f9b34fb | read    | Manufactuer Name String  | "Airthings AS"                |
| 00002a27-0000-1000-8000-00805f9b34fb | read    | Harwdare Revision String | (e.g. "REV A")                |
| 00002a26-0000-1000-8000-00805f9b34fb | read    | Firmware Revision String | (e.g. "G-BLE-1.4.5-beta+0")   |
| 00002a25-0000-1000-8000-00805f9b34fb | read    | Serial Number String     | (e.g. "029677")               |
| 00002a24-0000-1000-8000-00805f9b34fb | read    | Model Number String      | (e.g. "2950")                 |
| 00002a23-0000-1000-8000-00805f9b34fb | read    | System ID                | (e.g. `E4 61 00 00 Ed 04 18`) |

When combined, the `Model Number String` and `Serial Number String` appear to match the information provided in the BLE metadata `manufacturer_data`, as well as the serial printed on the physical device.

#### Airthings Wave Devices

| Characteristic UUID                  | Actions                                 | Description               |
| :---                                 | :---                                    | :---                      |
| b42e2a68-ade7-11e4-89d3-123b93f75cba | read                                    | Wave+ current readings    |
| b42e2fc2-ade7-11e4-89d3-123b93f75cba | notify                                  | Wave+                     |
| b42e2d06-ade7-11e4-89d3-123b93f75cba | write-without-response, write, indicate | Wave+                     |
| b42e4dcc-ade7-11e4-89d3-123b93f75cba | read                                    | Wave2 current readings    |
| b42e50d8-ade7-11e4-89d3-123b93f75cba | write, notify                           | Wave2                     |
| b42e538a-ade7-11e4-89d3-123b93f75cba | notify                                  | Wave2                     |
| b42e3b98-ade7-11e4-89d3-123b93f75cba | read                                    | WaveMini current readings |

#### TI OTA

| Characteristic UUID                  | Actions       | Description |
| :---                                 | :---          | :---        |
| f000ffc5-0451-4000-b000-000000000000 | write, notify | ?           |
| f000ffc2-0451-4000-b000-000000000000 | write, notify | ?           |
| f000ffc1-0451-4000-b000-000000000000 | write, notify | ?           |

## Data Formats

All binary data appears to be little-endian.

### BLE Manufacturer Data

The BLE advertisement's manufacturer data for Airthings devices (id: 820) encodes the device serial number, which itself embeds the device model.

`manufacturer_data(820)` (6 bytes, e.g. `0x6DE1D5AF0900`)

| Byte | Name   | Type   | Value / Example   | Notes                                        |
| :--- | :---   | :---   | :---              | :---                                         |
| 0-3  | serial | uint32 | e.g. `0x6DE1D5AF` | decimal: `2950029677` --> model 2950 (Wave2) |
| 4-5  | --     | --     | `0x0900`          | unknown, may vary                            |

### Wave (2900) Sensor Format
### Wave Mini (2920) Sensor Format
### Wave+ (2930) Sensor Format
### Wave2 (2950) Sensor Format

Reading BLE characteristic `b42e4dcc-ade7-11e4-89d3-123b93f75cba` returns a 20 byte value representing the current sensor values.

| Byte  | Name        | Type   | Notes                                       |
| :---  | :---        | :---   | :---                                        |
| 0     | version     | uint8  | sensor version, always `0x01`               |
| 1     | humidity    | uint8  | relative humidty = value/2 (percent)        |
| 2-3   | --          | --     | unknown, varies                             |
| 4-5   | radon\_sta  | uint16 | radon short-term average (Bq/m<sup>3</sup>) |
| 6-7   | radon\_lta  | uint16 | radon long-term average (Bq/m<sup>3</sup>)  |
| 8-9   | temperature | uint16 | temp = val/100 (celsius)                    |
| 10-19 | --          | --     | unknown, always `0xFFFFFFFFFFFF0000FFFF`    |

#### Sample Values

```
      0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19
#1 : 01 35 1d 00 28 00 3A 00 a2 07 ff ff ff ff ff ff 00 00 ff ff
#2 : 01 35 21 00 28 00 3A 00 9f 07 ff ff ff ff ff ff 00 00 ff ff
#3 : 01 35 3F 00 27 00 3A 00 96 07 ff ff ff ff ff ff 00 00 ff ff
```

Above sample for `#3`:

```
version = 1
relative humidity = 26.5%
short-term radon = 39 Bq^3
long-term radon = 58 Bq^3
temperature = 19.42°C
```

## Firmware Revisions

### Wave2
```
G-BLE-1.4.5-beta+0
G-BLE-1.5.3-master+0
```
