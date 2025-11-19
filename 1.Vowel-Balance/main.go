package main

func isBalanced(s string) bool {
	vowels := map[rune]bool{
		'a': true, 'e': true, 'i': true, 'o': true, 'u': true,
		'A': true, 'E': true, 'I': true, 'O': true, 'U': true,
	}

	r := []rune(s)
	n := len(r)
	half := n / 2
	balance := 0

	for i := 0; i < half; i++ {
		if vowels[r[i]] {
			balance++
		}
		if vowels[r[n-1-i]] {
			balance--
		}
	}

	return balance == 0
}
