package main

import (
	"slices"
	"strings"
)

func jbelmu(text string) string {
	words := strings.Fields(text)

	for i, w := range words {
		runes := []rune(w)
		if len(runes) <= 2 {
			continue
		}

		middle := runes[1 : len(runes)-1]
		slices.Sort(middle)
		words[i] = string(runes[0]) + string(middle) + string(runes[len(runes)-1])
	}

	return strings.Join(words, " ")
}
