import re

def is_valid_number(n, base):
    if base < 2 or base > 36:
        return False

    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    allowed = digits[:base]
    pattern = f'^[{allowed}]+$'

    return re.fullmatch(pattern, n, re.IGNORECASE) is not None