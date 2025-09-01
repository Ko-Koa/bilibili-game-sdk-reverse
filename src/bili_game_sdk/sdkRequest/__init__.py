from typing import Unpack

from bili_game_sdk.sdkRequest.request import Request
from bili_game_sdk.middlewares.signMiddleware import SignMiddleware
from bili_game_sdk.sdkRequest.typings import RequestMethod, BiliRequest
from bili_game_sdk.sdkRequest.downloaders.requestsDownloader import RequestsDownloader


def request(url: str, method: RequestMethod, **kwargs: Unpack[BiliRequest]):
    # 加载中间件
    middleware = SignMiddleware()

    # 创建请求对象
    request = Request(url=url, method=method, **kwargs)

    middleware.before_requests(request=request)

    response = RequestsDownloader().fetch(request=request)

    middleware.after_requests(response=response)

    return response


def post(url: str, **kwargs: Unpack[BiliRequest]):
    return request(url=url, method="POST", **kwargs)


def get(url: str, **kwargs: Unpack[BiliRequest]):
    return request(url=url, method="GET", **kwargs)


def delete(url: str, **kwargs: Unpack[BiliRequest]):
    return request(url=url, method="DELETE", **kwargs)


def put(url: str, **kwargs: Unpack[BiliRequest]):
    return request(url=url, method="PUT", **kwargs)
