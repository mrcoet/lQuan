from typing import Any
import aiohttp
from sqlalchemy.util import await_only
from web3 import HTTPProvider
from web3.types import RPCEndpoint, RPCResponse
from eth_typing import URI
from web3 import Web3

from keys import bsc_url_main_1

class AIOHTTPProvider(HTTPProvider):
    def make_request(self, method: RPCEndpoint, params: Any) -> RPCResponse:
        self.logger.debug("Making request HTTP. URI: %s, Method: %s", self.endpoint_uri, method)
        request_data = self.encode_rpc_request(method, params)
        raw_response = await_only(make_post_request(self.endpoint_uri, request_data, **self.get_request_kwargs()))
        response = self.decode_rpc_response(raw_response)
        self.logger.debug("Getting response HTTP. URI: %s, " "Method: %s, Response: %s", self.endpoint_uri, method, response)
        return response


async def make_post_request(endpoint_uri: URI, data: bytes, *args: Any, **kwargs: Any) -> bytes:
    kwargs.setdefault("timeout", 600)
    async with aiohttp.ClientSession() as client:
        response = await client.post(endpoint_uri, data=data, *args, **kwargs)  # type: ignore
        response.raise_for_status()
        return await response.content.read()


def get_w3():
    provider = AIOHTTPProvider(bsc_url_main_1)
    return Web3(provider=provider)
