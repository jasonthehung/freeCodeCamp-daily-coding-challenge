def is_valid_number(n, base):
    if base < 2 or base > 36:
        return False

    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    allowedSet = set(digits[:base])

    for char in n.upper():
        if char not in allowedSet:
            return False
        
    return True