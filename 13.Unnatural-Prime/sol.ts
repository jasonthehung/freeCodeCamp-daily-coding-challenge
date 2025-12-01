import * as fs from "fs";

// ======================================================================
// 🧠 CHALLENGE: Unnatural Prime
// ======================================================================
// Description:
// Given an integer, determine if that number is a prime number or a
// negative prime number.
//
// 📋 Rules:
// 1. A prime number is a positive integer greater than 1 that is only
//    divisible by 1 and itself.
// 2. A negative prime number is the negative version of a positive prime.
// 3. 0, 1, and -1 are NOT considered prime numbers.
// 4. Return true if the number is an "unnatural prime", false otherwise.
//
// 💡 Examples:
// - isUnnaturalPrime(19)   => true
// - isUnnaturalPrime(-23)  => true  (23 is prime)
// - isUnnaturalPrime(1)    => false
// - isUnnaturalPrime(0)    => false
// - isUnnaturalPrime(-44)  => false
// ======================================================================

// #region [📚 Reference Solutions]

/**
 * Method: Trial Division
 * Best for: General usage.
 * Complexity: Time O(sqrt(n))
 */
function isUnnaturalPrime1(n: number): boolean {
  // 1. Normalize using absolute value
  const absN = Math.abs(n);

  // 2. 0, 1 are not prime
  if (absN < 2) return false;

  // 3. Standard optimizations
  if (absN === 2 || absN === 3) return true;
  if (absN % 2 === 0 || absN % 3 === 0) return false;

  // 4. Loop up to square root
  // i * i <= absN is more efficient than Math.sqrt(absN) in loop condition
  for (let i = 5; i * i <= absN; i += 6) {
    if (absN % i === 0 || absN % (i + 2) === 0) {
      return false;
    }
  }

  return true;
}

// #endregion

// ======================================================================
//  #region [✍️ Practice Area]
//  Please write your solution between the markers below.
// ======================================================================
// <PRACTICE_START>
function isUnnaturalPrime(n: number): boolean {
  // TODO: Implement your solution here.
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
    "function isUnnaturalPrime(n: number): boolean {",
    "  // TODO: Implement your solution here.",
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
  expected: boolean;
};

function runTests() {
  const testCases: TestCase[] = [
    { n: 1, expected: false },
    { n: -1, expected: false },
    { n: 19, expected: true },
    { n: -23, expected: true },
    { n: 0, expected: false },
    { n: 97, expected: true },
    { n: -61, expected: true },
    { n: 99, expected: false },
    { n: -44, expected: false },
  ];

  console.log(`\n🧪 Testing your [isUnnaturalPrime] function...\n`);

  const pad = (str: string, len: number) =>
    (str + " ".repeat(len)).slice(0, len);

  const header = `${pad("Input", 8)} | ${pad("Expected", 10)} | ${pad(
    "Actual",
    10
  )} | Status`;
  console.log(header);
  console.log("-".repeat(header.length));

  let allPass = true;

  testCases.forEach(({ n, expected }) => {
    let result: any;
    try {
      result = isUnnaturalPrime(n);
    } catch (e) {
      result = "Error";
    }

    const isMatch = result === expected;
    const statusIcon = isMatch ? "✅ PASS" : "❌ FAIL";

    if (!isMatch) allPass = false;

    console.log(
      `${pad(String(n), 8)} | ${pad(String(expected), 10)} | ${pad(
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
