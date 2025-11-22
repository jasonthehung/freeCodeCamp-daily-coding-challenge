from collections import Counter

def are_anagrams(str1: str, str2: str) -> bool:
    """
    檢查兩個字串是否為變位詞 (Anagrams)，忽略大小寫和空白字符。
    
    :param str1: 第一個輸入字串
    :param str2: 第二個輸入字串
    :return: 如果是變位詞則回傳 True，否則回傳 False
    """
    
    # 1. 前處理 (Preprocessing): 轉換為小寫並移除所有空白
    # (使用 join 和 split 更簡潔地移除所有空白，或使用正則表達式)
    s1 = "".join(str1.lower().split())
    s2 = "".join(str2.lower().split())

    # 2. 長度檢查
    if len(s1) != len(s2):
        return False

    # 3. 使用 collections.Counter (這是 Python 中實現 Map/哈希表計數最慣用的方式)
    
    # 建立第一個字串 s1 的字符計數器
    char_counts = Counter(s1)

    # 4. 根據第二個字串 s2 進行驗證
    for char in s2:
        # 檢查字符是否存在
        if char not in char_counts:
            return False
        
        # 遞減計數
        char_counts[char] -= 1
        
        # 檢查計數是否變為負值（表示 s2 中該字符數量過多）
        if char_counts[char] < 0:
            return False

    # 5. 如果迴圈完成，表示它們是變位詞
    # 由於前面已經檢查過長度，並且沒有計數低於零的情況，
    # 剩下的所有計數都必須是零。
    return True

