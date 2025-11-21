package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestSomething(t *testing.T) {
	assert.Equal(
		t,
		jbelmu("hello world"),
		"hello wlord",
	)

	assert.Equal(
		t,
		jbelmu("freecodecamp is my favorite place to learn to code"),
		"faccdeeemorp is my faiortve pacle to laern to cdoe",
	)

	assert.Equal(
		t,
		jbelmu("the quick brown fox jumps over the lazy dog"),
		"the qciuk borwn fox jmpus oevr the lazy dog",
	)

	assert.Equal(
		t,
		jbelmu("i love jumbled text"),
		"i love jbelmud text",
	)
}
