import asyncio

from wave_reader.web.api.devices import device_info
from wave_reader.web.client import AuthenticatedClient, OAuth2ClientHandler


async def get_battery_information(serial: str, client: AuthenticatedClient):
    return await device_info.asyncio_detailed(serial, client=client)


if __name__ == "__main__":
    serial = input("Serial of device: ")
    client_id = input("Enter your Airthings OAuth client ID: ")
    client_secret = input("Enter your Airthings OAuth client secret: ")

    handler = OAuth2ClientHandler(client_id, client_secret, "127.0.0.1")
    handler.new_authorization_url()
    handler.new_access_token()
    client = handler.new_client()

    loop = asyncio.new_event_loop()
    data = loop.run_until_complete(get_battery_information(serial, client))
    print(data)
