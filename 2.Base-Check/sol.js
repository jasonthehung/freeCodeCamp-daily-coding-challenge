const fs = require("fs");

// ======================================================================
// 🧠 CHALLENGE: Base Check (JavaScript Version)
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

const DIGITS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";

// #region [📚 Reference Solutions] (Fold this region to hide answers)

/**
 * Method 1: Regular Expressions
 * Best for: Defining complex string patterns compactly.
 */
function solution1_Regex(n, base) {
  if (base < 2 || base > 36) return false;

  // Slice the allowed characters string
  const allowed = DIGITS.slice(0, base);

  // Construct Regex: ^[allowed]+$ with 'i' flag for case-insensitivity
  const pattern = new RegExp(`^[${allowed}]+$`, "i");

  return pattern.test(n);
}

/**
 * Method 2: Set / Lookup (High Performance)
 * Best for: Algorithmic clarity and O(N) performance.
 */
function solution2_Set(n, base) {
  if (base < 2 || base > 36) return false;

  // Create a Set for O(1) lookup time
  const allowedSet = new Set(DIGITS.slice(0, base));

  for (let char of n.toUpperCase()) {
    if (!allowedSet.has(char)) {
      return false;
    }
  }
  return true;
}

/**
 * Method 3: Functional / Array Method (Modern JS)
 * Best for: Clean, readable one-liners.
 */
function solution3_Functional(n, base) {
  if (base < 2 || base > 36) return false;

  const allowed = DIGITS.slice(0, base);
  // Check if every character in input is included in the allowed string
  return [...n.toUpperCase()].every((char) => allowed.includes(char));
}

// #endregion

// ======================================================================
//  #region [✍️ Practice Area]
//  Please write your solution between the markers below.
// ======================================================================
// <PRACTICE_START>
function isValidNumber(n, base) {
  // TODO: Implement your solution here.
  // (This function will automatically reset once you pass all tests)
  return false;
}
// <PRACTICE_END>
// #endregion

// ======================================================================
//  #region [🚀 Test Runner & Auto-Reset] (Do not modify below this line)
// ======================================================================

function resetPracticeArea() {
  console.log("\n🔄 Resetting Practice Area to default state...");

  const MARKER_START = "// <PRACTICE_" + "START>";
  const MARKER_END = "// <PRACTICE_" + "END>";

  const defaultCode = [
    "function isValidNumber(n, base) {",
    "  // TODO: Implement your solution here.",
    "  // (This function will automatically reset once you pass all tests)",
    "  return false;",
    "}",
  ].join("\n");

  try {
    const currentFile = __filename;
    const content = fs.readFileSync(currentFile, "utf8");
    const lines = content.split("\n");

    let startIdx = -1;
    let endIdx = -1;

    lines.forEach((line, index) => {
      if (line.includes(MARKER_START)) startIdx = index;
      if (line.includes(MARKER_END)) endIdx = index;
    });

    if (startIdx === -1 || endIdx === -1 || startIdx >= endIdx) {
      console.log("⚠️ Error: Markers not found or invalid. Reset cancelled.");
      return;
    }

    // Reconstruct file content
    const newLines = [
      ...lines.slice(0, startIdx + 1),
      defaultCode,
      ...lines.slice(endIdx),
    ];

    fs.writeFileSync(currentFile, newLines.join("\n"), "utf8");
    console.log("✨ Reset complete! The file is ready for a fresh start.");
  } catch (e) {
    console.log(`⚠️ Reset failed: ${e.message}`);
  }
}

function runTests() {
  const testCases = [
    { n: "10101", base: 2, expected: true },
    { n: "10201", base: 2, expected: false }, // '2' invalid in base 2
    { n: "76543210", base: 8, expected: true },
    { n: "9876543210", base: 8, expected: false }, // '8','9' invalid
    { n: "9876543210", base: 10, expected: true },
    { n: "ABC", base: 10, expected: false },
    { n: "ABC", base: 16, expected: true },
    { n: "Z", base: 36, expected: true },
    { n: "ABC", base: 20, expected: true },
    { n: "4B4BA9", base: 16, expected: true },
    { n: "5G3F8F", base: 16, expected: false }, // 'G' invalid in base 16
    { n: "5G3F8F", base: 17, expected: true }, // 'G' valid in base 17
    { n: "abc", base: 10, expected: false },
    { n: "abc", base: 16, expected: true }, // Lowercase check
    { n: "AbC", base: 16, expected: true }, // Mixed case check
    { n: "z", base: 36, expected: true },
  ];

  console.log(`\n🧪 Testing your [isValidNumber] function...\n`);

  // Formatter helpers
  const pad = (str, len) => (str + " ".repeat(len)).slice(0, len);

  const header = `${pad("Input", 12)} | ${pad("Base", 6)} | ${pad(
    "Exp",
    6
  )} | ${pad("Act", 6)} | Status`;
  console.log(header);
  console.log("-".repeat(header.length));

  let allPass = true;

  testCases.forEach(({ n, base, expected }) => {
    let result;
    try {
      result = isValidNumber(n, base);
    } catch (e) {
      result = "Error";
    }

    const statusIcon = result === expected ? "✅ PASS" : "❌ FAIL";
    if (result !== expected) allPass = false;

    console.log(
      `${pad(n, 12)} | ${pad(String(base), 6)} | ${pad(
        String(expected),
        6
      )} | ${pad(String(result), 6)} | ${statusIcon}`
    );
  });

  console.log("-".repeat(header.length));

  if (allPass) {
    console.log("\n🎉 Fantastic! All test cases passed.");
    resetPracticeArea();
  } else {
    console.log(
      "\n⚠️  Some tests failed. Keep trying! (The file will not reset yet)"
    );
  }
}

// Execute
runTests();

// #endregion
