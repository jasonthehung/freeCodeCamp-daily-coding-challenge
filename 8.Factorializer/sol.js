const fs = require("fs");

// ======================================================================
// 🧠 CHALLENGE: Factorializer
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
// - factorial(0)  => 1
// - factorial(5)  => 120  (5 * 4 * 3 * 2 * 1)
// - factorial(20) => 2432902008176640000
// ======================================================================

// #region [📚 Reference Solutions] (Solutions hidden as requested)
// (Focus on implementing your own logic in the Practice Area below!)
// #endregion

// ======================================================================
//  #region [✍️ Practice Area]
//  Please write your solution between the markers below.
// ======================================================================
// <PRACTICE_START>
function factorial(n) {
  // TODO: Implement your solution here.
  return 0;
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
    "function factorial(n) {",
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
    { n: 0, expected: 1 },
    { n: 1, expected: 1 },
    { n: 5, expected: 120 },
    { n: 10, expected: 3628800 },
    { n: 20, expected: 2432902008176640000 },
  ];

  console.log(`\n🧪 Testing your [factorial] function...\n`);

  const pad = (str, len) => (str + " ".repeat(len)).slice(0, len);

  const header = `${pad("Input (n)", 10)} | ${pad("Expected", 20)} | ${pad(
    "Actual",
    20
  )} | Status`;
  console.log(header);
  console.log("-".repeat(header.length));

  let allPass = true;

  testCases.forEach(({ n, expected }) => {
    let result;
    try {
      result = factorial(n);
    } catch (e) {
      result = "Error";
    }

    // Note: For n=20, JS numbers (floats) are precise enough because the number ends in many zeros.
    const isMatch = result === expected;
    const statusIcon = isMatch ? "✅ PASS" : "❌ FAIL";

    if (!isMatch) allPass = false;

    console.log(
      `${pad(String(n), 10)} | ${pad(String(expected), 20)} | ${pad(
        String(result),
        20
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
