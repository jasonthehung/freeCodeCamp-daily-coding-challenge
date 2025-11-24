package main

func isVowel(c rune) bool {
	switch c {
	case 'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U':
		return true
	}
	return false
}

func isBalanced(s string) bool {
	r := []rune(s)
	n := len(r)
	half := n / 2
	balance := 0

	for i := 0; i < half; i++ {
		if isVowel(r[i]) {
			balance++
		}
		if isVowel(r[n-1-i]) {
			balance--
		}
	}

	return balance == 0
}
