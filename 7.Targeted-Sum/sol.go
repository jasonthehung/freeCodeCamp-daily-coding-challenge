package main

import (
	"fmt"
	"os"
	"reflect"
	"runtime"
	"strings"
)

// ======================================================================
// 🧠 CHALLENGE: Targeted Sum (Go Version)
// ======================================================================
// Description:
// Given an array of numbers and an integer target, find two unique numbers
// in the array that add up to the target value.
//
// 📋 Rules:
// 1. Return a slice containing the INDICES of the two numbers.
// 2. The indices in the result must be in ascending order (e.g., [0, 1]).
// 3. You may not use the same element (same index) twice.
// 4. If no two numbers sum up to the target, return string "Target not found".
//
// 💡 Examples:
// - FindTarget([2, 7, 11, 15], 9)      => [0, 1]
// - FindTarget([3, 2, 4, 5], 6)        => [1, 2]
// - FindTarget([1, 3, 5, 6, 7, 8], 15) => [4, 5]
// - FindTarget([1, 3, 5, 7], 14)       => "Target not found"
// ======================================================================

// #region [📚 Reference Solutions] (Solutions hidden as requested)

// (Reference solutions have been removed.)
// (Focus on implementing your own logic in the Practice Area below!)

// #endregion

// ======================================================================
//  #region [✍️ Practice Area]
//  Please write your solution between the markers below.
// ======================================================================
// <PRACTICE_START>
func FindTarget(nums []int, target int) interface{} {
	// TODO: Implement your solution here.
	// Note: Return type is interface{} to allow returning []int OR string.
	// (This function will automatically reset once you pass all tests)
	return "Target not found"
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
	nums     []int
	target   int
	expected interface{}
}

func runTests() {
	testCases := []TestCase{
		{[]int{2, 7, 11, 15}, 9, []int{0, 1}},
		{[]int{3, 2, 4, 5}, 6, []int{1, 2}},
		{[]int{1, 3, 5, 6, 7, 8}, 15, []int{4, 5}},
		{[]int{1, 3, 5, 7}, 14, "Target not found"},
	}

	fmt.Printf("\n🧪 Testing your [FindTarget] function...\n\n")

	// Helper to format output
	fmtVal := func(v interface{}) string {
		return fmt.Sprintf("%v", v)
	}

	header := fmt.Sprintf("%-20s | %-6s | %-18s | %-18s | Status", "Input Array", "Target", "Expected", "Actual")
	fmt.Println(header)
	fmt.Println(strings.Repeat("-", len(header)))

	allPass := true

	for _, tc := range testCases {
		result := FindTarget(tc.nums, tc.target)

		// Check equality using reflect because of interface{} type
		isMatch := reflect.DeepEqual(result, tc.expected)
		statusIcon := "✅ PASS"
		if !isMatch {
			statusIcon = "❌ FAIL"
			allPass = false
		}

		numsStr := fmtVal(tc.nums)
		if len(numsStr) > 18 {
			numsStr = numsStr[:15] + "..."
		}

		fmt.Printf("%-20s | %-6d | %-18s | %-18s | %s\n",
			numsStr, tc.target, fmtVal(tc.expected), fmtVal(result), statusIcon)
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
		"func FindTarget(nums []int, target int) interface{} {",
		"\t// TODO: Implement your solution here.",
		"\t// Note: Return type is interface{} to allow returning []int OR string.",
		"\t// (This function will automatically reset once you pass all tests)",
		"\treturn \"Target not found\"",
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