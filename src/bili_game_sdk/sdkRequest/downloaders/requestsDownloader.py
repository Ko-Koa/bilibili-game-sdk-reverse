import requests

from bili_game_sdk.sdkRequest.request import Request
from bili_game_sdk.sdkRequest.response import Response
from bili_game_sdk.sdkRequest.downloaders.baseDownloader import BaseDownloader


class RequestsDownloader(BaseDownloader):
    def fetch(self, request: Request) -> Response:

        response = requests.request(
            method=request.method,
            url=request.url,
            params=request.param,
            data=request.data,
            json=request.json,
            headers=request.headers,
            cookies=request.cookeis,
            proxies=request.proxy,
            timeout=request.timeout,
            verify=request.verify,
        )

        return Response(
            response=response,
            url=response.url,
            status_code=response.status_code,
            content=response.content,
            headers=dict(response.headers),
            cookies=requests.utils.dict_from_cookiejar(response.cookies),
            encoding=str(response.encoding),
        )
