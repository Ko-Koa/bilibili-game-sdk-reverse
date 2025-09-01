from bili_game_sdk.sdkRequest.request import Request
from bili_game_sdk.utils.sdkUtils import generate_sign
from bili_game_sdk.sdkRequest.baseMiddleware import BaseMiddleware


class SignMiddleware(BaseMiddleware):
    def before_requests(self, request: Request):
        # 给data加签名
        data = request.data
        if data is not None and not isinstance(data, str):
            sign = generate_sign(data=data)
            data["sign"] = sign

            request.data = data

        # param加签名
        param = request.param
        if param is not None:
            sign = generate_sign(data=param)
            param["sign"] = sign

            request.param = param
