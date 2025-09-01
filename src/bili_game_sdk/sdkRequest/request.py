from typing import Any

from bili_game_sdk.sdkRequest.typings import RequestMethod


class Request(object):
    def __init__(
        self,
        url: str,
        method: RequestMethod,
        param: dict[str, Any] | None = None,
        data: dict[str, Any] | str | None = None,
        json: dict[str, Any] | None = None,
        headers: dict[str, Any] | None = None,
        cookies: dict[str, Any] | None = None,
        proxy: dict[str, Any] | None = None,
        timeout: int | None = None,
        verify: bool | None = None,
    ) -> None:
        self.url = url
        self.method = method
        self.param = param
        self.data = data
        self.json = json
        self.headers = headers
        self.cookeis = cookies
        self.proxy = proxy
        self.timeout = timeout
        self.verify = verify
