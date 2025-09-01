from abc import ABC, abstractmethod

from bili_game_sdk.sdkRequest.request import Request
from bili_game_sdk.sdkRequest.response import Response


class BaseDownloader(ABC):
    @abstractmethod
    def fetch(self, request: Request) -> Response: ...
