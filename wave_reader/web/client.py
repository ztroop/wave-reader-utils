import logging
import ssl
from typing import Dict, Optional, Union

import attr
from authlib.integrations.httpx_client import OAuth2Client


@attr.s(auto_attribs=True)
class Client:
    """A class for keeping track of data related to the API"""

    base_url: str
    cookies: Dict[str, str] = attr.ib(factory=dict, kw_only=True)
    headers: Dict[str, str] = attr.ib(factory=dict, kw_only=True)
    timeout: float = attr.ib(5.0, kw_only=True)
    verify_ssl: Union[str, bool, ssl.SSLContext] = attr.ib(True, kw_only=True)

    def get_headers(self) -> Dict[str, str]:
        """Get headers to be used in all endpoints"""
        return {**self.headers}

    def with_headers(self, headers: Dict[str, str]) -> "Client":
        """Get a new client matching this one with additional headers"""
        return attr.evolve(self, headers={**self.headers, **headers})

    def get_cookies(self) -> Dict[str, str]:
        return {**self.cookies}

    def with_cookies(self, cookies: Dict[str, str]) -> "Client":
        """Get a new client matching this one with additional cookies"""
        return attr.evolve(self, cookies={**self.cookies, **cookies})

    def get_timeout(self) -> float:
        return self.timeout

    def with_timeout(self, timeout: float) -> "Client":
        """Get a new client matching this one with a new timeout (in seconds)"""
        return attr.evolve(self, timeout=timeout)


@attr.s(auto_attribs=True)
class AuthenticatedClient(Client):
    """A Client which has been authenticated for use on secured endpoints"""

    token: str
    prefix: str = "Bearer"
    auth_header_name: str = "Authorization"

    def get_headers(self) -> Dict[str, str]:
        auth_header_value = f"{self.prefix} {self.token}" if self.prefix else self.token
        """Get headers to be used in authenticated endpoints"""
        return {self.auth_header_name: auth_header_value, **self.headers}


class OAuth2ClientHandler:
    """A class that handles OAuth2 authentication with convenience methods."""

    authorization_url = "https://accounts.airthings.com/authorize"
    token_url = "https://accounts-api.airthings.com/v1/token"
    base_url = "https://ext-api.airthings.com/v1/"

    def __init__(self, client_id: str, client_secret: str, redirect_uri: str):
        self.logger = logging.getLogger(__name__)
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
        self.oauth = OAuth2Client(
            client_id=self.client_id,
            client_secret=self.client_secret,
            redirect_uri=self.redirect_uri,
        )
        self.client: Optional[AuthenticatedClient] = None
        self.token: str = ""
        self.token_expires_at: Optional[int] = None

    def new_authorization_url(self) -> str:
        """Generate an authorization URL and state."""

        try:
            authorization, _ = self.oauth.create_authorization_url(
                self.authorization_url
            )
            return authorization
        except Exception:
            self.logger.error("Error occurred: Check your token details are correct.")
            return ""

    def new_access_token(self) -> str:
        """Fetch an access token from the token endpoint."""

        try:
            token = self.oauth.fetch_token(self.token_url)
            self.token = token.get("access_token")
            self.token_expires_at = token.get("expires_at")
            return self.token
        except Exception as err:
            self.logger.error(f"Error occurred: {err}")
            return ""

    def new_client(self) -> AuthenticatedClient:
        """Generate an AuthenticatedClient with token details."""

        self.client = AuthenticatedClient(self.base_url, self.token)
        return self.client
