import time
from datetime import datetime

def get_current_timestamp(is_ms: bool = True) -> int:
    """获取当前时间戳

    Args:
        is_ms (bool, optional): 是否为毫秒. Defaults to True.
    """
    if is_ms:
        return round(time.time() * 1000)
    return round(time.time())


def convert_timestamp_to_time(timestamp: int, is_ms: bool = True, fmt:str = "%Y-%m-%d %H:%M:%S") -> str:
    timestamp_ = timestamp
    if is_ms:
        timestamp_ = timestamp / 1000
    dt_obj = datetime.fromtimestamp(timestamp_)
    return dt_obj.strftime(fmt)
