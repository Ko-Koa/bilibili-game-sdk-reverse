import re
import uuid
import base64
import hashlib

from loguru import logger
from getmac import get_mac_address


def salt(md5_str: str):
    return md5_str[2] + md5_str[12] + md5_str[22]


def get_wifi_mac():
    wifi_mac = get_mac_address("wlan")
    if wifi_mac is None:
        wifi_mac = get_mac_address()
        if wifi_mac is None:
            raise Exception("获取mac失败")
    return wifi_mac.upper()


def get_buvid():
    # "XZ"开头 => IMEI; XY => wifi mac ;"XX" => AndroidId "XW" => uuid
    wifi_mac = get_wifi_mac()
    md5 = hashlib.new("md5")
    md5.update(wifi_mac.upper().encode())
    md5_str = md5.digest().hex()
    buvid = "XY" + salt(md5_str) + md5_str
    return buvid.upper()


def get_device_bd_id():
    buvid = get_buvid()
    bd_id_raw = f"{uuid.uuid4()}-{buvid.lower()}"
    buid = bd_id_raw[:64]
    return buid


def get_udid():
    wifi_mac = get_wifi_mac()
    wifi_mac_replace = re.sub("[^0-9A-Fa-f]", "", wifi_mac).lower()
    plaintext = f"{wifi_mac_replace}|||"
    bytes_arr = bytearray(plaintext.encode("utf-8"))
    length = len(bytes_arr)
    bytes_arr[0] = bytes_arr[0] ^ (length & 0xFF) & 0xFF
    for i in range(1, length):
        bytes_arr[i] = (bytes_arr[i - 1] ^ bytes_arr[i]) & 0xFF
    return base64.b64encode(bytes_arr).decode("utf-8")


def get_hwid():
    wifi_mac = get_wifi_mac()
    md5 = hashlib.new("md5")
    md5.update(wifi_mac.upper().encode())
    md5_str = md5.digest().hex()
    return "EA" + md5_str
