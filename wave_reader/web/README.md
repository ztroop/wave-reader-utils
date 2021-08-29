# Airthings Web API Client

A client library for accessing Airthings Web API.

## Usage

First, create a client:

```python
from wave_reader.web import client

client = client.OAuth2ClientHandler(client_id, client_secret, redirect_uri)
client.new_authorization_url()
client.new_access_token()
```

Now call your endpoint and use the models:

```python
from wave_reader.web.models.get_device_detailed_response import GetDeviceDetailedResponse
from wave_reader.api.devices import device_info
from wave_reader.web.types import Response

response: Response[GetDeviceDetailedResponse] = device_info.sync_detailed(1234567890, client=client)
```

Or do the same thing with an async version:

```python
from wave_reader.web.models.get_device_detailed_response import GetDeviceDetailedResponse
from wave_reader.api.devices import device_info
from wave_reader.web.types import Response

response: Response[GetDeviceDetailedResponse] = await device_info.asyncio_detailed(1234567890, client=client)
```

Things to Know:
1. Every path/method combo becomes a Python module with four functions:
    - `sync`: Blocking request that returns parsed data (if successful) or `None`
    - `sync_detailed`: Blocking request that always returns a `Request`, optionally with `parsed` set if the request was successful.
    - `asyncio`: Like `sync` but the async instead of blocking
    - `asyncio_detailed`: Like `sync_detailed` by async instead of blocking

2. All path/query params, and bodies become method arguments.
3. If your endpoint had any tags on it, the first tag will be used as a module name for the function (my_tag above)
4. Any endpoint which did not have a tag will be in `airthings_api_client.api.default`
