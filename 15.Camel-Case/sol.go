package main

import (
	"fmt"
	"os"
	"runtime"
	"strings"
	"unicode"
)

// ======================================================================
// 🧠 CHALLENGE: camelCase (Go Version)
// ======================================================================
// Description:
// Given a string, return its camel case version using the following rules:
// 1. Words are separated by spaces ( ), dashes (-), or underscores (_).
// 2. Treat any sequence of these characters as a single word break.
// 3. The first word should be all lowercase.
// 4. Each subsequent word should start with an uppercase letter,
//    with the rest of it lowercase.
// 5. All spaces and separators should be removed.
//
// 💡 Examples:
// - ToCamelCase("hello world")       => "helloWorld"
// - ToCamelCase("HELLO WORLD")       => "helloWorld"
// - ToCamelCase("secret agent-X")    => "secretAgentX"
// - ToCamelCase("FREE cODE cAMP")    => "freeCodeCamp"
// ======================================================================

// #region [📚 Reference Solutions] (Solutions hidden as requested)

func ToCamelCase1(text string) string {
	// 1. Define a splitter function for FieldsFunc
	// Returns true if the character is a separator
	isSeparator := func(r rune) bool {
		return r == ' ' || r == '-' || r == '_'
	}

	// 2. Split into words (FieldsFunc handles multiple consecutive separators automatically)
	words := strings.FieldsFunc(text, isSeparator)

	if len(words) == 0 {
		return ""
	}

	// Use StringBuilder for efficient concatenation
	var sb strings.Builder

	for i, word := range words {
		// Normalize word to all lowercase first to handle inputs like "HELLO"
		lowerWord := strings.ToLower(word)

		if i == 0 {
			// 3. First word: all lowercase
			sb.WriteString(lowerWord)
		} else {
			// 4. Subsequent words: capitalize first letter
			// We convert the first byte to uppercase (safe for standard ASCII a-z)
			// For full Unicode support, we would use unicode.ToUpper(rune)
			runes := []rune(lowerWord)
			runes[0] = unicode.ToUpper(runes[0])
			sb.WriteString(string(runes))
		}
	}

	return sb.String()
}

// #endregion

// ======================================================================
//
//	#region [✍️ Practice Area]
//	Please write your solution between the markers below.
//
// ======================================================================
// <PRACTICE_START>
func ToCamelCase(s string) string {
	// TODO: Implement your solution here.
	return ""
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
	str      string
	expected string
}

func runTests() {
	testCases := []TestCase{
		{"hello world", "helloWorld"},
		{"HELLO WORLD", "helloWorld"},
		{"secret agent-X", "secretAgentX"},
		{"FREE cODE cAMP", "freeCodeCamp"},
		{"ye old-_-sea  faring_buccaneer_-_with a - peg__leg----and a_parrot_ _named- _squawk",
			"yeOldSeaFaringBuccaneerWithAPegLegAndAParrotNamedSquawk"},
	}

	fmt.Printf("\n🧪 Testing your [ToCamelCase] function...\n\n")

	header := fmt.Sprintf("%-25s | %-20s | %-20s | Status", "Input String", "Expected", "Actual")
	fmt.Println(header)
	fmt.Println(strings.Repeat("-", len(header)))

	allPass := true

	for _, tc := range testCases {
		result := ToCamelCase(tc.str)

		isMatch := result == tc.expected
		statusIcon := "✅ PASS"
		if !isMatch {
			statusIcon = "❌ FAIL"
			allPass = false
		}

		trunc := func(s string, length int) string {
			if len(s) > length {
				return s[:length-3] + "..."
			}
			return s
		}

		fmt.Printf("%-25s | %-20s | %-20s | %s\n",
			trunc(tc.str, 25), trunc(tc.expected, 20), trunc(result, 20), statusIcon)
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
		"func ToCamelCase(s string) string {",
		"\t// TODO: Implement your solution here.",
		"\treturn \"\"",
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
