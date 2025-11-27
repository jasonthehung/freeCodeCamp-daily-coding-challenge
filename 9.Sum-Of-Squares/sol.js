const fs = require("fs");

// ======================================================================
// 🧠 CHALLENGE: Sum of Squares
// ======================================================================
// Description:
// Given a positive integer n (up to 1,000), return the sum of all the
// integers squared from 1 up to n.
//
// Formula: 1² + 2² + 3² + ... + n²
//
// 📋 Rules:
// 1. n will be a positive integer between 1 and 1,000.
// 2. Return the calculated sum.
//
// 💡 Examples:
// - sumOfSquares(5)    => 55  (1 + 4 + 9 + 16 + 25)
// - sumOfSquares(10)   => 385
// - sumOfSquares(1000) => 333833500
// ======================================================================

// #region [📚 Reference Solutions] (Solutions hidden as requested)

/**
 * Method 1: Iterative Approach
 */
function sumOfSquares_Iterative(n) {
  let res = 0;
  for (let i = 1; i <= n; i++) {
    res += i * i;
  }
  return res;
}

/**
 * Method 2: Mathematical Formula (Optimal)
 * Note: Returns an integer result instantly.
 */
function sumOfSquares_Math(n) {
  return (n * (n + 1) * (2 * n + 1)) / 6;
}
// #endregion

// ======================================================================
//  #region [✍️ Practice Area]
//  Please write your solution between the markers below.
// ======================================================================
// <PRACTICE_START>
function sumOfSquares(n) {
  return n * (n + 1) * ((n + 2) / 6);
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
    "function sumOfSquares(n) {",
    "  // TODO: Implement your solution here.",
    "  return 0;",
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
    { n: 5, expected: 55 },
    { n: 10, expected: 385 },
    { n: 25, expected: 5525 },
    { n: 500, expected: 41791750 },
    { n: 1000, expected: 333833500 },
  ];

  console.log(`\n🧪 Testing your [sumOfSquares] function...\n`);

  const pad = (str, len) => (str + " ".repeat(len)).slice(0, len);

  const header = `${pad("Input (n)", 10)} | ${pad("Expected", 15)} | ${pad(
    "Actual",
    15
  )} | Status`;
  console.log(header);
  console.log("-".repeat(header.length));

  let allPass = true;

  testCases.forEach(({ n, expected }) => {
    let result;
    try {
      result = sumOfSquares(n);
    } catch (e) {
      result = "Error";
    }

    const isMatch = result === expected;
    const statusIcon = isMatch ? "✅ PASS" : "❌ FAIL";

    if (!isMatch) allPass = false;

    console.log(
      `${pad(String(n), 10)} | ${pad(String(expected), 15)} | ${pad(
        String(result),
        15
      )} | ${statusIcon}`
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

runTests();

// #endregion
