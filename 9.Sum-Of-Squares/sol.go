package main

import (
	"fmt"
	"os"
	"runtime"
	"strings"
)

// ======================================================================
// 🧠 CHALLENGE: Factorializer (Go Version)
// ======================================================================
// Description:
// Given an integer n (from 0 to 20), return the factorial of that number.
// The factorial of a number is the product of all positive integers
// less than or equal to n.
//
// 📋 Rules:
// 1. n will be an integer between 0 and 20.
// 2. factorial(0) is defined as 1.
// 3. Return the calculated factorial value.
//
// 💡 Examples:
// - Factorial(0)  => 1
// - Factorial(5)  => 120  (5 * 4 * 3 * 2 * 1)
// - Factorial(20) => 2432902008176640000
// ======================================================================

// #region [📚 Reference Solutions] (Solutions hidden as requested)

/**
 * Method 1: Iterative Approach
 */
func SumOfSquaresIterative(n int) int {
	res := 0
	for i := 1; i <= n; i++ {
		res += i * i
	}
	return res
}

/**
 * Method 2: Mathematical Formula (Optimal)
 * Best for: Constant time complexity O(1).
 */
func SumOfSquaresMath(n int) int {
	return (n * (n + 1) * (2*n + 1)) / 6
}

// #endregion

// ======================================================================
//
//	#region [✍️ Practice Area]
//	Please write your solution between the markers below.
//
// ======================================================================
// <PRACTICE_START>
func Factorial(n int) int64 {
	// TODO: Implement your solution here.
	return 0
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
	expected int64
}

func runTests() {
	testCases := []TestCase{
		{0, 1},
		{1, 1},
		{5, 120},
		{10, 3628800},
		{20, 2432902008176640000},
	}

	fmt.Printf("\n🧪 Testing your [Factorial] function...\n\n")

	header := fmt.Sprintf("%-10s | %-20s | %-20s | Status", "Input (n)", "Expected", "Actual")
	fmt.Println(header)
	fmt.Println(strings.Repeat("-", len(header)))

	allPass := true

	for _, tc := range testCases {
		result := Factorial(tc.n)

		isMatch := result == tc.expected
		statusIcon := "✅ PASS"
		if !isMatch {
			statusIcon = "❌ FAIL"
			allPass = false
		}

		fmt.Printf("%-10d | %-20d | %-20d | %s\n",
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
		"func Factorial(n int) int64 {",
		"\t// TODO: Implement your solution here.",
		"\treturn 0",
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
