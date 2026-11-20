import string
import time
import random
from datetime import datetime

def get_random_email() -> str:
    return f"test.{time.time()}@example.com"
def get_random_letter() -> str:
    return random.choice(string.ascii_letters + string.digits)
def get_string_AQA_type_date(name_type: str = "string") -> str:
    now = datetime.now()
    time_str = now.strftime("%H:%M")  # 13:50
    date_str = now.strftime("%d.%m.%Y")  # 15.10.2026
    return f"AQA {name_type} {time_str} {date_str}"

def get_len_string_AQA_type_date(name_type: str = "string", length: int | None = None) -> str:
    now = datetime.now()
    time_str = now.strftime("%H:%M")        # 21:19
    date_str = now.strftime("%d.%m.%Y")     # 20.11.2026
    result = f"AQA {name_type} {time_str} {date_str}"

    if length is None:
        return result
    if length <= 0:
        raise ValueError(f"length должен быть положительным числом, получено: {length}")

    if len(result) < length:
        # дополняем случайными латинскими буквами и цифрами до нужной длины
        charset = string.ascii_lowercase + string.digits   # a-z и 0-9
        tail = "".join(random.choices(charset, k=length - len(result)))
        return result + tail
    return result[:length]  # обрезаем до нужной длины