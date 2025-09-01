import base64

from loguru import logger
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5

from bili_game_sdk import sdkRequest
from bili_game_sdk.typings import CipherInfo
from bili_game_sdk.utils.sdkUtils import get_bd_info
from bili_game_sdk.config.sdkConfig import BSGameSdkConfig
from bili_game_sdk.utils.timeUtils import get_current_timestamp
from bili_game_sdk.utils.deviceUtils import (
    get_buvid,
    get_device_bd_id,
    get_hwid,
    get_wifi_mac,
    get_udid,
)


def external_issue_cipher_v3() -> CipherInfo:
    headers = {
        "user-agent": "Mozilla/5.0 BSGameSDK",
    }
    url = "https://line1-sdk-center-login-sh.biligame.net/api/external/issue/cipher/v3"
    data = {
        "merchant_id": BSGameSdkConfig.MERCHANT_ID,
        "game_id": BSGameSdkConfig.APP_ID,
        "timestamp": str(get_current_timestamp()),
        "cipher_type": "bili_login_rsa",
        "server_id": BSGameSdkConfig.SERVER_ID,
        "version": "3",
    }
    response = sdkRequest.post(url, headers=headers, data=data)
    resonse_data = response.json()
    if resonse_data.get("code") != 0:
        raise Exception(f"Request faild, Response:\n{resonse_data}")

    return {
        "hashCode": resonse_data.get("hash"),
        "rsaKey": resonse_data.get("cipher_key"),
    }


def external_login_v3(user_id: str, password: str, cipher_info: CipherInfo, bd_id: str):
    # rsa encrypt password
    salt_password = cipher_info["hashCode"] + password
    key = RSA.import_key(cipher_info["rsaKey"])
    padding_rsa = PKCS1_v1_5.new(key)
    pwd_row = padding_rsa.encrypt(salt_password.encode("utf-8"))
    pwd = base64.b64encode(pwd_row).decode("utf-8")

    headers = {
        "user-agent": "Mozilla/5.0 BSGameSDK",
    }

    url = "https://line1-sdk-center-login-sh.biligame.net/api/external/login/v3"

    data = {
        "merchant_id": BSGameSdkConfig.MERCHANT_ID,
        "game_id": BSGameSdkConfig.APP_ID,
        "timestamp": str(get_current_timestamp()),
        "bd_id": bd_id,
        "server_id": BSGameSdkConfig.SERVER_ID,
        "version": "3",
        "user_id": user_id,
        "pwd": pwd,
    }
    response = sdkRequest.post(url, headers=headers, data=data)
    return response.json()


def client_activate():
    timestamp = str(get_current_timestamp())

    # generate buvid and bd_id
    buvbid = get_buvid()
    bd_id = get_device_bd_id()

    # Device Info
    device_info = {
        "cur_buvid": buvbid,
        "old_buvid": buvbid,
        "udid": get_udid(),
        "bd_id": bd_id,
        "imei": "",
        "mac": get_wifi_mac(),
        "android_id": "a33db2dab3a0ec80",
        "oaid": "aafc70c5cc148b40",
        "model": "MIX 3",
        "brand": "Xiaomi",
        "dp": "2030,1080,440",
        "net": "1",
        "operators": "中国移动",
        "supportedAbis": "[arm64-v8a, armeabi-v7a, armeabi]",
        "is_root": "0",
        "pf_ver": "9",
        "platform_type": "Android",
        "ver": "1.0.55",
        "version_code": "110",
        "sdk_ver": "5.9.0",
        "app_id": BSGameSdkConfig.APP_ID,
        "fts": 0,
        "first": 0,
        "files": "",
        "pkg_name": "",
        "app_name": "",
        "finger_print": "Xiaomi/chiron/chiron:9/PKQ1.190118.001/9.9.3:user/release-keys",
        "serial": "unknown",
        "band": "AT20-0827_0009_2705804,AT20-0827_0009_2705804",
        "cpu_count": 8,
        "cpu_model": "AArch64 Processor rev 1 (aarch64)",
        "cpu_freq": 1900800,
        "cpu_verdor": "Qualcomm",
        "sensor": '{"1":"ICM20690 Accelerometer -Wakeup Secondary","35":"ICM20690 Accelerometer Uncalibrated -Wakeup Secondary","2":"AK09918 Magnetometer -Wakeup Secondary","14":"AK09918 Magnetometer Uncalibrated -Wakeup Secondary","4":"ICM20690 Gyroscope -Wakeup Secondary","16":"ICM20690 Gyroscope Uncalibrated -Wakeup Secondary","6":"BMP285 Pressure -Wakeup Secondary","9":"Gravity -Wakeup Secondary","10":"Linear Acceleration -Wakeup Secondary","11":"Rotation Vector -Wakeup Secondary","18":"Step Detector -Wakeup Secondary","19":"Step Counter -Wakeup Secondary","17":"Significant Motion Detector","15":"Game Rotation Vector -Wakeup Secondary","20":"GeoMagnetic Rotation Vector -Wakeup Secondary","3":"Orientation -Wakeup Secondary","22":"Tilt Detector","29":"Android Stationary Detector","30":"Android Motion Detector","33171036":"pickup  Wakeup","33171027":"Oem7 NoneUi","33171006":"AMD","33171007":"RMD","33171009":"Pedometer","33171011":"Motion Accel","5":"BH1745 BH1745 ALS DEVICE","33171022":"DPC","33171023":"MultiShake","8":"Elliptic Proximity"}',
        "camcnt": 2,
        "campx": "4000x3000",
        "camzoom": "4.5",
        "bat_level": "100",
        "bat_state": "2",
        "ts": timestamp,
        "brightness": 1040,
        "boot": 347487608,
        "total_ram": 6002499584,
        "total_rom": 117990408192,
        "is_debug": "1",
        "is_emu": "000000",
        "time_zone": "GMT+08:00 TimeZone id :Asia/Shanghai",
        "lang": "ZH",
        "os": "android",
        "hwId": get_hwid(),
        "kernel_ver": "4.4.153-perf+",
    }

    # get bd_info
    bd_info = get_bd_info(device_info)

    # activate cookie
    headers = {"cversion": "1", "one-sdk-ver": "null", "user-agent": "okhttp/3.12.1"}
    url = "https://p.biligame.com/api/client/activate"
    data = {
        "merchant_id": BSGameSdkConfig.MERCHANT_ID,
        "game_id": BSGameSdkConfig.APP_ID,
        "timestamp": timestamp,
        "bd_id": bd_id,
        "server_id": BSGameSdkConfig.SERVER_ID,
        "version": "1",
        "bd_info": bd_info,
        "channel_id": "1",
    }
    response = sdkRequest.post(url, headers=headers, data=data)
    code = response.json().get("code")
    if code == 0:
        logger.success("Activate bd_id success")
        return bd_id

    logger.error("Activate bd_id Faild")
    return None
