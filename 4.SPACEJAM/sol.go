package main

import (
	"strings"
	"unicode"
)

func spaceJam(s string) string {
	var noSpace strings.Builder
	for _, r := range s {
		if !unicode.IsSpace(r) {
			noSpace.WriteRune(r)
		}
	}

	upper := strings.ToUpper(noSpace.String())

	result := strings.Join(strings.Split(upper, ""), "  ")

	return result
}
