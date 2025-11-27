import * as fs from "fs";

// ======================================================================
// 🧠 CHALLENGE: 3 Strikes
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
// - squaresWithThree(1)   => 0   (1^2 = 1, no '3')
// - squaresWithThree(10)  => 1   (Only 6^2 = 36 contains '3')
// - squaresWithThree(100) => 19
// ======================================================================

// #region [📚 Reference Solutions] (Solutions hidden as requested)

/**
 * Method: Mathematical (Modulo & Trunc)
 * Best for: High performance. Avoids string conversion overhead.
 * Complexity: Time O(N) | Space O(1)
 */
function squaresWithThree_Math(n: number): number {
  let count = 0;

  for (let i = 1; i <= n; i++) {
    let square = i * i;

    while (square > 0) {
      // Check last digit
      if (square % 10 === 3) {
        count++;
        break;
      }
      // Remove last digit using Math.trunc
      square = Math.trunc(square / 10);
    }
  }
  return count;
}
// #endregion

// ======================================================================
//  #region [✍️ Practice Area]
//  Please write your solution between the markers below.
// ======================================================================
// <PRACTICE_START>
function squaresWithThree(n: number): number {
  let count = 0;

  for (let i = 1; i <= n; i++) {
    let square = i * i;

    while (square > 0) {
      if (square % 10 === 3) {
        count++;
        break;
      }
      square = Math.trunc(square / 10);
    }
  }

  return count;
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
    "function squaresWithThree(n: number): number {",
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
  } catch (e: any) {
    console.log(`⚠️ Reset failed: ${e.message}`);
  }
}

type TestCase = {
  n: number;
  expected: number;
};

function runTests() {
  const testCases: TestCase[] = [
    { n: 1, expected: 0 },
    { n: 10, expected: 1 },
    { n: 100, expected: 19 },
    { n: 1000, expected: 326 },
    { n: 10000, expected: 4531 },
  ];

  console.log(`\n🧪 Testing your [squaresWithThree] function...\n`);

  const pad = (str: string, len: number) =>
    (str + " ".repeat(len)).slice(0, len);

  const header = `${pad("Input (n)", 10)} | ${pad("Expected", 10)} | ${pad(
    "Actual",
    10
  )} | Status`;
  console.log(header);
  console.log("-".repeat(header.length));

  let allPass = true;

  testCases.forEach(({ n, expected }) => {
    let result: any;
    try {
      result = squaresWithThree(n);
    } catch (e) {
      result = "Error";
    }

    const isMatch = result === expected;
    const statusIcon = isMatch ? "✅ PASS" : "❌ FAIL";

    if (!isMatch) allPass = false;

    console.log(
      `${pad(String(n), 10)} | ${pad(String(expected), 10)} | ${pad(
        String(result),
        10
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
