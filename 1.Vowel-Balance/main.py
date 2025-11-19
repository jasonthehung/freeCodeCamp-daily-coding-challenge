def is_balanced(s):
    vowels = set("aeiouAEIOU")
    n = len(s)
    half = n // 2
    balance = 0

    for i in range(half):
        if s[i] in vowels:
            balance += 1
        if s[n - 1 - i] in vowels:
            balance -= 1

    return balance == 0