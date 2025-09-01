from bili_game_sdk.sdkRequest.request import Request
from bili_game_sdk.sdkRequest.response import Response


class BaseMiddleware(object):
    def before_requests(self, request: Request): ...

    def after_requests(self, response: Response): ...
