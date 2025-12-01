package main

import (
	"fmt"
	"os"
	"runtime"
	"strings"
)

// ======================================================================
// 🧠 CHALLENGE: Unnatural Prime (Go Version)
// ======================================================================
// Description:
// Given an integer, determine if that number is a prime number or a
// negative prime number.
//
// 📋 Rules:
// 1. A prime number is a positive integer greater than 1 that is only
//    divisible by 1 and itself.
// 2. A negative prime number is the negative version of a positive prime.
// 3. 0, 1, and -1 are NOT considered prime numbers.
// 4. Return true if the number is an "unnatural prime", false otherwise.
//
// 💡 Examples:
// - IsUnnaturalPrime(19)   => true
// - IsUnnaturalPrime(-23)  => true  (23 is prime)
// - IsUnnaturalPrime(1)    => false
// - IsUnnaturalPrime(0)    => false
// - IsUnnaturalPrime(-44)  => false
// ======================================================================

// #region [📚 Reference Solutions] (Solutions hidden as requested)
// (Focus on implementing your own logic in the Practice Area below!)
// #endregion

// ======================================================================
//
//	#region [✍️ Practice Area]
//	Please write your solution between the markers below.
//
// ======================================================================
// <PRACTICE_START>
func IsUnnaturalPrime(n int) bool {
	// TODO: Implement your solution here.
	return false
}

// <PRACTICE_END>
// #endregion

// ======================================================================
//  #region [🚀 Test Runner & Auto-Reset] (Do not modify below this line)
// ======================================================================

func main() {
	runTests()
}

type TestCase struct {
	n        int
	expected bool
}

func runTests() {
	testCases := []TestCase{
		{1, false},
		{-1, false},
		{19, true},
		{-23, true},
		{0, false},
		{97, true},
		{-61, true},
		{99, false},
		{-44, false},
	}

	fmt.Printf("\n🧪 Testing your [IsUnnaturalPrime] function...\n\n")

	header := fmt.Sprintf("%-8s | %-10s | %-10s | Status", "Input", "Expected", "Actual")
	fmt.Println(header)
	fmt.Println(strings.Repeat("-", len(header)))

	allPass := true

	for _, tc := range testCases {
		result := IsUnnaturalPrime(tc.n)

		isMatch := result == tc.expected
		statusIcon := "✅ PASS"
		if !isMatch {
			statusIcon = "❌ FAIL"
			allPass = false
		}

		fmt.Printf("%-8d | %-10v | %-10v | %s\n",
			tc.n, tc.expected, result, statusIcon)
	}

	fmt.Println(strings.Repeat("-", len(header)))

	if allPass {
		fmt.Println("\n🎉 Fantastic! All test cases passed.")
		resetPracticeArea()
	} else {
		fmt.Println("\n⚠️  Some tests failed. Keep trying! (The file will not reset yet)")
	}
}

func resetPracticeArea() {
	fmt.Println("\n🔄 Resetting Practice Area to default state...")

	markerStart := "// <PRACTICE_" + "START>"
	markerEnd := "// <PRACTICE_" + "END>"

	defaultCode := []string{
		"func IsUnnaturalPrime(n int) bool {",
		"\t// TODO: Implement your solution here.",
		"\treturn false",
		"}",
	}

	_, currentFile, _, ok := runtime.Caller(0)
	if !ok {
		fmt.Println("⚠️ Error: Could not determine file path. Reset cancelled.")
		return
	}

	content, err := os.ReadFile(currentFile)
	if err != nil {
		fmt.Printf("⚠️ Error reading file: %v\n", err)
		return
	}

	lines := strings.Split(string(content), "\n")
	startIdx := -1
	endIdx := -1

	for i, line := range lines {
		if strings.Contains(line, markerStart) {
			startIdx = i
		} else if strings.Contains(line, markerEnd) {
			endIdx = i
		}
	}

	if startIdx == -1 || endIdx == -1 || startIdx >= endIdx {
		fmt.Println("⚠️ Error: Markers not found or invalid. Reset cancelled.")
		return
	}

	newLines := make([]string, 0)
	newLines = append(newLines, lines[:startIdx+1]...)
	newLines = append(newLines, defaultCode...)
	newLines = append(newLines, lines[endIdx:]...)

	output := strings.Join(newLines, "\n")
	err = os.WriteFile(currentFile, []byte(output), 0644)
	if err != nil {
		fmt.Printf("⚠️ Error writing file: %v\n", err)
		return
	}

	fmt.Println("✨ Reset complete! The file is ready for a fresh start.")
}

// #endregion
