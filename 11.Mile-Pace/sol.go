package main

import (
	"fmt"
	"math"
	"os"
	"runtime"
	"strconv"
	"strings"
)

// ======================================================================
// 🧠 CHALLENGE: Mile Pace (Go Version)
// ======================================================================
// Description:
// Given a distance in miles (number) and a total time in "MM:SS" format,
// return the average pace per mile as a string in "MM:SS" format.
//
// 📋 Rules:
// 1. Return the average time it took to run each mile.
// 2. The output format must be "MM:SS".
// 3. Ensure leading zeros are added where needed (e.g., "04:36", not "4:36").
// 4. Round the seconds to the nearest whole number.
//
// 💡 Examples:
// - MilePace(3, "24:00")     => "08:00"
// - MilePace(1, "06:45")     => "06:45"
// - MilePace(2, "07:00")     => "03:30"
// - MilePace(26.2, "120:35") => "04:36"
// ======================================================================

// #region [📚 Reference Solutions] (Solutions hidden as requested)

func MilePace1(distance float64, timeStr string) string {
	// 1. Split and Parse
	parts := strings.Split(timeStr, ":")
	min, _ := strconv.Atoi(parts[0])
	sec, _ := strconv.Atoi(parts[1])

	// 2. Total seconds (cast to float for division)
	totalSeconds := float64((min * 60) + sec)

	// 3. Math.Round matches the JS/TS behavior
	paceSeconds := math.Round(totalSeconds / distance)

	// 4. Convert back to int
	finalMin := int(paceSeconds) / 60
	finalSec := int(paceSeconds) % 60

	// 5. Format using Sprintf with %02d (padding)
	return fmt.Sprintf("%02d:%02d", finalMin, finalSec)
}

// #endregion

// ======================================================================
//
//	#region [✍️ Practice Area]
//	Please write your solution between the markers below.
//
// ======================================================================
// <PRACTICE_START>
func MilePace(miles float64, timeStr string) string {
	// TODO: Implement your solution here.
	return "00:00"
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
	miles    float64
	time     string
	expected string
}

func runTests() {
	testCases := []TestCase{
		{3, "24:00", "08:00"},
		{1, "06:45", "06:45"},
		{2, "07:00", "03:30"},
		{26.2, "120:35", "04:36"},
	}

	fmt.Printf("\n🧪 Testing your [MilePace] function...\n\n")

	header := fmt.Sprintf("%-8s | %-8s | %-10s | %-10s | Status", "Miles", "Time", "Expected", "Actual")
	fmt.Println(header)
	fmt.Println(strings.Repeat("-", len(header)))

	allPass := true

	for _, tc := range testCases {
		result := MilePace(tc.miles, tc.time)

		isMatch := result == tc.expected
		statusIcon := "✅ PASS"
		if !isMatch {
			statusIcon = "❌ FAIL"
			allPass = false
		}

		fmt.Printf("%-8v | %-8s | %-10s | %-10s | %s\n",
			tc.miles, tc.time, tc.expected, result, statusIcon)
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
		"func MilePace(miles float64, timeStr string) string {",
		"\t// TODO: Implement your solution here.",
		"\treturn \"00:00\"",
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
