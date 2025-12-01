package main

import (
	"fmt"
	"os"
	"runtime"
	"strings"
)

// ======================================================================
// 🧠 CHALLENGE: Message Decoder (Go Version)
// ======================================================================
// Description:
// Given a secret message string and an integer representing the shift amount
// used to encode it, return the decoded string.
//
// 📋 Rules:
// 1. The `shift` value represents how many positions letters were moved
//    to ENCODE the message. (e.g., shift 1 means A -> B).
// 2. To DECODE, you must shift in the opposite direction.
// 3. Positive shift = Encoded forward. Negative shift = Encoded backward.
// 4. Preserve case (Upper/Lower) and non-alphabetical characters.
// 5. Handle wrapping (A -> Z, Z -> A).
//
// 💡 Examples:
// - Decode("Xlmw mw...", 4)  => "This is..." ('X' is 'T' shifted +4, so go back 4)
// - Decode("Byffi...", 20)   => "Hello..."
// - Decode("Zqd...", -1)     => "Are..."     (Encoded -1, so shift +1 to decode)
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
func Decode(message string, shift int) string {
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
	message  string
	shift    int
	expected string
}

func runTests() {
	testCases := []TestCase{
		{"Xlmw mw e wigvix qiwweki.", 4, "This is a secret message."},
		{"Byffi Qilfx!", 20, "Hello World!"},
		{"Zqd xnt njzx?", -1, "Are you okay?"},
		{"oannLxmnLjvy", 9, "freeCodeCamp"},
	}

	fmt.Printf("\n🧪 Testing your [Decode] function...\n\n")

	header := fmt.Sprintf("%-20s | %-6s | %-20s | %-20s | Status", "Input Message", "Shift", "Expected", "Actual")
	fmt.Println(header)
	fmt.Println(strings.Repeat("-", len(header)))

	allPass := true

	for _, tc := range testCases {
		result := Decode(tc.message, tc.shift)

		isMatch := result == tc.expected
		statusIcon := "✅ PASS"
		if !isMatch {
			statusIcon = "❌ FAIL"
			allPass = false
		}

		msgStr := tc.message
		if len(msgStr) > 18 {
			msgStr = msgStr[:15] + "..."
		}
		expStr := tc.expected
		if len(expStr) > 18 {
			expStr = expStr[:15] + "..."
		}
		resStr := result
		if len(resStr) > 18 {
			resStr = resStr[:15] + "..."
		}

		fmt.Printf("%-20s | %-6d | %-20s | %-20s | %s\n",
			msgStr, tc.shift, expStr, resStr, statusIcon)
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
		"func Decode(message string, shift int) string {",
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
