package main

func FibonacciSequence(startSequence []int, length int) []int {
	if length <= 0 {
		return []int{}
	}

	if len(startSequence) >= length {
		return startSequence[:length]
	}

	result := make([]int, len(startSequence))
	copy(result, startSequence)

	for len(result) < length {
		last := result[len(result)-1]
		secondLast := result[len(result)-2]
		result = append(result, last+secondLast)
	}

	return result
}
