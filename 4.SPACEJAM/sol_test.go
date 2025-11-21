package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestSomething(t *testing.T) {
	assert.Equal(
		t,
		spaceJam("freeCodeCamp"),
		"F  R  E  E  C  O  D  E  C  A  M  P",
	)

	assert.Equal(
		t,
		spaceJam("   free   Code   Camp   "),
		"F  R  E  E  C  O  D  E  C  A  M  P",
	)

	assert.Equal(
		t,
		spaceJam("C@t$ & D0g$"),
		"C  @  T  $  &  D  0  G  $",
	)

	assert.Equal(
		t,
		spaceJam("allyourbase"),
		"A  L  L  Y  O  U  R  B  A  S  E",
	)
}
