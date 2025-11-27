package main

import (
	"fmt"
	"os"
	"runtime"
	"strings"
)

// ======================================================================
// 🧠 CHALLENGE: 3 Strikes (Go Version)
// ======================================================================
// Description:
// Given an integer n (between 1 and 10,000), return a count of how many
// numbers from 1 up to n (inclusive) have a square that contains
// at least one digit '3'.
//
// 📋 Rules:
// 1. n will be an integer between 1 and 10,000.
// 2. Calculate the square of each number from 1 to n.
// 3. Check if the string representation of that square contains the character '3'.
// 4. Return the count of such numbers.
//
// 💡 Examples:
// - SquaresWithThree(1)   => 0   (1^2 = 1, no '3')
// - SquaresWithThree(10)  => 1   (Only 6^2 = 36 contains '3')
// - SquaresWithThree(100) => 19
// ======================================================================

// #region [📚 Reference Solutions]

/**
 * Method: Mathematical (Integer Division)
 * Best for: Strict O(1) space complexity.
 */
func SquaresWithThreeMath(n int) int {
	count := 0
	for i := 1; i <= n; i++ {
		square := i * i
		temp := square // Use temp to preserve 'square' if needed elsewhere

		for temp > 0 {
			if temp%10 == 3 {
				count++
				break
			}
			// In Go, integer division automatically truncates
			temp /= 10
		}
	}
	return count
}

// #endregion

// ======================================================================
//
//	#region [✍️ Practice Area]
//	Please write your solution between the markers below.
//
// ======================================================================
// <PRACTICE_START>
func SquaresWithThree(n int) int {
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
	expected int
}

func runTests() {
	testCases := []TestCase{
		{1, 0},
		{10, 1},
		{100, 19},
		{1000, 326},
		{10000, 4531},
	}

	fmt.Printf("\n🧪 Testing your [SquaresWithThree] function...\n\n")

	header := fmt.Sprintf("%-10s | %-10s | %-10s | Status", "Input (n)", "Expected", "Actual")
	fmt.Println(header)
	fmt.Println(strings.Repeat("-", len(header)))

	allPass := true

	for _, tc := range testCases {
		result := SquaresWithThree(tc.n)

		isMatch := result == tc.expected
		statusIcon := "✅ PASS"
		if !isMatch {
			statusIcon = "❌ FAIL"
			allPass = false
		}

		fmt.Printf("%-10d | %-10d | %-10d | %s\n",
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
		"func SquaresWithThree(n int) int {",
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
