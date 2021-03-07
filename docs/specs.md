# Device Specifications

While Airthings has been kind enough to provide sample code for interfacing with
their Wave family of devices, most of the technical details have to be inferred
from the code or discovered via experimentation. This is an unofficial attempt to
document those specifications, in hopes that they may be useful to other projects.

## Models

| Model    | Product Name   | Serial     | Sensors
| :---     | :---           | :---       | :---
| 2900     | Wave           | 2900xxxxxx | radon, temperature, humidity
| 2920     | Wave Mini      | 2920xxxxxx | temperature, humidity, TVOCs, CO<sub>2</sub>
| 2930     | Wave Plus      | 2930xxxxxx | radon, temperature, humidity, TVOCs, CO<sub>2</sub>
| 2950     | Wave (2nd gen) | 2950xxxxxx | radon, temperature, humidity
| 2940     | Wave Mist      | 2940xxxxxx | ?
| 2810     | Wave Hub       | 2810xxxxxx | ?
| 2820     | Wave Hub       | 2820xxxxxx | ?

## Bluetooth Low Energy (BLE)

## BLE Advertisement

A standard BLE advertisement contains 4 attributes: `name`, `address`, `rssi`, and `metadata`.

### BLE Advertisement - Name

The `name` attribute *may* be populated with an Airthings name based on the model.

| Model  | BLE Advertised Name
| :---   | :---
| 2900   | Airthings Wave (not verified)
| 2920   | Airthings Wave Mini (not verified)
| 2930   | Airthings Wave+
| 2940   | Airthings Wave Mist (not verified)
| 2950   | Airthings Wave2

Advertisements are **not guaranteed** to be populated with this descriptive
name, possibly appearing as a variant of the MAC address (e.g. `12-34-56-78-90-AD`).

### BLE Advertisement - Metadata

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

## BLE Services

**Wave+**

| Service UUID                         | Description                      | Notes                       |
| :---                                 | :---                             | :---                        |
| 00001801-0000-1000-8000-00805f9b34fb | Generic Attribute Profile        |                             |
| 0000180a-0000-1000-8000-00805f9b34fb | Device Information               |                             |
| f000ffc0-0451-4000-b000-000000000000 | TI Over-the-Air Download Service | Likely Firmware Related     |
| b42e1c08-ade7-11e4-89d3-123b93f75cba | Unknown (Airthings)              | Wave+                       |

**Wave2**

| Service UUID                         | Description                      | Notes                       |
| :---                                 | :---                             | :---                        |
| 00001801-0000-1000-8000-00805f9b34fb | Generic Attribute Profile        |                             |
| 0000180a-0000-1000-8000-00805f9b34fb | Device Information               |                             |
| f000ffc0-0451-4000-b000-000000000000 | TI Over-the-Air Download Service | Likely Firmware Related     |
| b42e4a8e-ade7-11e4-89d3-123b93f75cba | Airthings                        | Wave2                       |

## BLE Characteristics

### Device Information Service

The ``characteristic`` UUIDs seem to be consistent on Wave2 and Wave+ devices.

| Characteristic UUID                  | Actions | Name                     | Value / Example               |
| :---                                 | :---    | :---                     | :---                          |
| 00002a29-0000-1000-8000-00805f9b34fb | read    | Manufactuer Name String  | "Airthings AS"                |
| 00002a27-0000-1000-8000-00805f9b34fb | read    | Harwdare Revision String | (e.g. "REV A")                |
| 00002a26-0000-1000-8000-00805f9b34fb | read    | Firmware Revision String | (e.g. "G-BLE-1.4.5-beta+0")   |
| 00002a25-0000-1000-8000-00805f9b34fb | read    | Serial Number String     | (e.g. "029677")               |
| 00002a24-0000-1000-8000-00805f9b34fb | read    | Model Number String      | (e.g. "2950")                 |
| 00002a23-0000-1000-8000-00805f9b34fb | read    | System ID                | (e.g. `E4 61 00 00 Ed 04 18`) |

When combined, the `Model Number String` and `Serial Number String` appear to match the information provided in the BLE metadata `manufacturer_data`, as well as the serial printed on the physical device.

### Airthings Service

**Wave+**

| Characteristic UUID                  | Actions                                 | Description               |
| :---                                 | :---                                    | :---                      |
| b42e2fc2-ade7-11e4-89d3-123b93f75cba | notify                                  |                           |
| b42e2d06-ade7-11e4-89d3-123b93f75cba | write-without-reponse, write, indicate  |                           |
| b42e2a68-ade7-11e4-89d3-123b93f75cba | read                                    | Wave+ current readings    |

**Wave2**

| Characteristic UUID                  | Actions                                 | Description               |
| :---                                 | :---                                    | :---                      |
| b42e538a-ade7-11e4-89d3-123b93f75cba | notify                                  |                           |
| b42e50d8-ade7-11e4-89d3-123b93f75cba | write, notify                           |                           |
| b42e4dcc-ade7-11e4-89d3-123b93f75cba | read                                    | Wave2 current readings    |

### TI Over-the-Air Download Service

**Wave+**

| Characteristic UUID                  | Actions                               | Description |
| :---                                 | :---                                  | :---        |
| f000ffc5-0451-4000-b000-000000000000 | write-without-response, notify        | ?           |
| f000ffc2-0451-4000-b000-000000000000 | write-without-response, write, notify | ?           |
| f000ffc1-0451-4000-b000-000000000000 | write-without-response, write, notify | ?           |

**Wave2**

| Characteristic UUID                  | Actions       | Description |
| :---                                 | :---          | :---        |
| f000ffc5-0451-4000-b000-000000000000 | write, notify | ?           |
| f000ffc2-0451-4000-b000-000000000000 | write, notify | ?           |
| f000ffc1-0451-4000-b000-000000000000 | write, notify | ?           |

# Data Format

All binary data appears to be little-endian.

## BLE Manufacturer Data

The BLE advertisement's manufacturer data for Airthings devices (id: 820) encodes the device serial number, which itself embeds the device model.

`manufacturer_data(820)` (6 bytes, e.g. `0x6DE1D5AF0900`)

| Byte | Name   | Type   | Value / Example   | Notes                                        |
| :--- | :---   | :---   | :---              | :---                                         |
| 0-3  | serial | uint32 | e.g. `0x6DE1D5AF` | decimal: `2950029677` --> model 2950 (Wave2) |
| 4-5  | --     | --     | `0x0900`          | unknown, may vary                            |

## Sensor Values

**Wave+**

Reading BLE characteristic `b42e4dcc-ade7-11e4-89d3-123b93f75cba` returns a 20 byte value representing the current sensor values.

```
00000000: 3031 2034 3120 3030 2030 3020 3838 2030  01 41 00 00 88 0
00000010: 3020 3866 2030 3020 3066 2030 3820 3538  0 8f 00 0f 08 58
00000020: 2062 6620 6234 2030 3220 3732 2030 3020   bf b4 02 72 00
00000030: 3030 2030 3020 3163 2030 360a            00 00 1c 06.
```

**Wave2**

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

```
00000000: 3031 2033 3520 3164 2030 3020 3238 2030  01 35 1d 00 28 0
00000010: 3020 3341 2030 3020 6132 2030 3720 6666  0 3A 00 a2 07 ff
00000020: 2066 6620 6666 2066 6620 6666 2066 6620   ff ff ff ff ff
00000030: 3030 2030 3020 6666 2066 660a            00 00 ff ff.
```
