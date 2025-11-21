package main

import (
	"sort"
	"strings"
)

func jbelmu(text string) string {
	words := strings.Fields(text)
	
	for i, w := range words {
		runes := []rune(w)
		if len(runes) <= 2 {
			continue
		}

		middle := runes[1 : len(runes) - 1]
		sort.Slice(middle, func(i, j int) bool { return middle[i] < middle[j] })
		words[i] = string(runes[0]) + string(middle) + string(runes[len(runes) - 1])
	}

	return strings.Join(words, " ")
}