import json
import base64
import hashlib
from typing import Any

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

from bili_game_sdk.config.sdkConfig import BSGameSdkConfig


def generate_sign(data: dict[str, str]) -> str:
    sorted_data = dict(sorted(data.items()))
    plaintext = ""
    for key, value in sorted_data.items():
        filter_key_list = ["item_name", "item_desc", "feign_sign", "token", "sign"]
        if key not in filter_key_list:
            plaintext += value

    app_key = BSGameSdkConfig.APP_Key
    md5 = hashlib.new("md5")
    md5.update(plaintext.encode("utf-8"))
    md5.update(app_key.encode("utf-8"))
    return md5.digest().hex()


def get_bd_info(device_info: dict[str, Any]):
    key = "68b9f18eac8f4e3b"  # 不确定会不会随版本变化， GSCPubCommon写死的
    info_text = json.dumps(device_info, separators=(",", ":"), ensure_ascii=False)
    info_text = info_text.replace("/", "\\/")  # 需要额外转义
    pad_plaintext = pad(info_text.encode(), 16)
    aes = AES.new(key=key.encode("utf-8"), mode=AES.MODE_ECB)
    cipher_raw = aes.encrypt(pad_plaintext)
    return "_v2_" + base64.b64encode(cipher_raw).decode()
