package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestSomething(t *testing.T) {
	assert.Equal(
		t,
		FibonacciSequence([]int{0, 1}, 20),
		[]int{0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181},
	)

	assert.Equal(
		t,
		FibonacciSequence([]int{21, 32}, 1),
		[]int{21},
	)

	assert.Equal(
		t,
		FibonacciSequence([]int{0, 1}, 0),
		[]int{},
	)

	assert.Equal(
		t,
		FibonacciSequence([]int{123456789, 987654321}, 5),
		[]int{123456789, 987654321, 1111111110, 2098765431, 3209876541},
	)
}
