package main

import "fmt"

func IsValidNumber(n string, base int) bool {
	// 1. 基礎檢查
	if base < 2 || base > 36 {
		return false
	}

	// 2. 遍歷字串
	for _, char := range n {
		var val int

		// 判斷字元並轉換為數值
		if char >= '0' && char <= '9' {
			val = int(char - '0')
		} else if char >= 'A' && char <= 'Z' {
			val = int(char-'A') + 10
		} else if char >= 'a' && char <= 'z' {
			val = int(char-'a') + 10
		} else {
			// 非數字也非字母，直接不合法
			return false
		}

		// 3. 檢查數值是否小於進位制
		if val >= base {
			return false
		}
	}

	return true
}

func main() {
	fmt.Println(IsValidNumber("1A", 16)) // true
	fmt.Println(IsValidNumber("1G", 16)) // false (G is 16, invalid for hex)
	fmt.Println(IsValidNumber("z", 36))  // true
	fmt.Println(IsValidNumber("Z", 36))  // true
}
