package main

import (
	"fmt"
	"os"
	"regexp"
	"runtime"
	"strconv"
	"strings"
)

// ======================================================================
// 🧠 CHALLENGE: Base Check (Go Version)
// ======================================================================
// Description:
// Given a string representing a number (n) and an integer base (from 2 to 36),
// determine whether the number is valid in that specific base.
//
// 📋 Rules:
// 1. The string 'n' may contain integers (0-9) and letters (A-Z).
// 2. The validation must be case-insensitive ('a' == 'A').
// 3. The 'base' will be an integer between 2 and 36.
// 4. Return true if valid, false otherwise.
// ======================================================================

const DIGITS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

// #region [📚 Reference Solutions] (Fold this region to hide answers)

// Solution 1: Standard Library (Simplest, but size limited)
// Note: This fails if the number string is larger than Int64 (overflow).
func solution1_StdLib(n string, base int) bool {
	if base < 2 || base > 36 {
		return false
	}
	// strconv.ParseInt checks validity, but also parses value.
	// It returns an error if the format is wrong OR if it overflows.
	_, err := strconv.ParseInt(n, base, 64)
	return err == nil
}

// Solution 2: Regex
// Good for validation rules, slower than loop.
func solution2_Regex(n string, base int) bool {
	if base < 2 || base > 36 {
		return false
	}
	allowed := DIGITS[:base]
	pattern := fmt.Sprintf("(?i)^[%s]+$", allowed) // (?i) = case insensitive
	match, _ := regexp.MatchString(pattern, n)
	return match
}

// Solution 3: Algorithmic / Rune Check
// Best for: Performance & handling arbitrarily long strings.
func solution3_Algorithmic(n string, base int) bool {
	if base < 2 || base > 36 {
		return false
	}
	for _, char := range n {
		var val int
		// Convert rune to integer value
		if char >= '0' && char <= '9' {
			val = int(char - '0')
		} else if char >= 'A' && char <= 'Z' {
			val = int(char - 'A') + 10
		} else if char >= 'a' && char <= 'z' {
			val = int(char - 'a') + 10
		} else {
			return false // Invalid character
		}

		// Check against base
		if val >= base {
			return false
		}
	}
	return true
}

// #endregion

// ======================================================================
//  #region [✍️ Practice Area]
//  Please write your solution between the markers below.
// ======================================================================
// <PRACTICE_START>
func IsValidNumber(n string, base int) bool {
	// TODO: Implement your solution here.
	// (This function will automatically reset once you pass all tests)
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
	n        string
	base     int
	expected bool
}

func runTests() {
	testCases := []TestCase{
		{"10101", 2, true},
		{"10201", 2, false},
		{"76543210", 8, true},
		{"9876543210", 8, false},
		{"9876543210", 10, true},
		{"ABC", 10, false},
		{"ABC", 16, true},
		{"Z", 36, true},
		{"ABC", 20, true},
		{"4B4BA9", 16, true},
		{"5G3F8F", 16, false},
		{"5G3F8F", 17, true},
		{"abc", 10, false},
		{"abc", 16, true},
		{"AbC", 16, true},
		{"z", 36, true},
	}

	fmt.Printf("\n🧪 Testing your [IsValidNumber] function...\n\n")

	// Table formatting
	fmt.Printf("%-12s | %-6s | %-8s | %-8s | Status\n", "Input", "Base", "Exp", "Act")
	fmt.Println(strings.Repeat("-", 56))

	allPass := true

	for _, tc := range testCases {
		result := IsValidNumber(tc.n, tc.base)

		status := "❌ FAIL"
		if result == tc.expected {
			status = "✅ PASS"
		} else {
			allPass = false
		}

		fmt.Printf("%-12s | %-6d | %-8v | %-8v | %s\n",
			tc.n, tc.base, tc.expected, result, status)
	}

	fmt.Println(strings.Repeat("-", 56))

	if allPass {
		fmt.Println("\n🎉 Fantastic! All test cases passed.")
		resetPracticeArea()
	} else {
		fmt.Println("\n⚠️  Some tests failed. Keep trying! (The file will not reset yet)")
	}
}

func resetPracticeArea() {
	fmt.Println("\n🔄 Resetting Practice Area to default state...")

	// Markers
	markerStart := "// <PRACTICE_" + "START>"
	markerEnd := "// <PRACTICE_" + "END>"

	// Default Code
	defaultCode := []string{
		"func IsValidNumber(n string, base int) bool {",
		"\t// TODO: Implement your solution here.",
		"\t// (This function will automatically reset once you pass all tests)",
		"\treturn false",
		"}",
	}

	// Get current file path using runtime.Caller
	_, currentFile, _, ok := runtime.Caller(0)
	if !ok {
		fmt.Println("⚠️ Error: Could not determine file path. Reset cancelled.")
		return
	}

	// Read file
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

	// Reconstruct content
	newLines := make([]string, 0)
	newLines = append(newLines, lines[:startIdx+1]...)
	newLines = append(newLines, defaultCode...)
	newLines = append(newLines, lines[endIdx:]...)

	// Write file
	output := strings.Join(newLines, "\n")
	err = os.WriteFile(currentFile, []byte(output), 0644)
	if err != nil {
		fmt.Printf("⚠️ Error writing file: %v\n", err)
		return
    }

	fmt.Println("✨ Reset complete! The file is ready for a fresh start.")
}

// #endregion