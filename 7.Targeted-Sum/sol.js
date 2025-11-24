const fs = require("fs");

// ======================================================================
// 🧠 CHALLENGE: Targeted Sum (JavaScript Version)
// ======================================================================
// Description:
// Given an array of numbers and an integer target, find two unique numbers
// in the array that add up to the target value.
//
// 📋 Rules:
// 1. Return an array containing the INDICES of the two numbers.
// 2. The indices in the result must be in ascending order (e.g., [0, 1]).
// 3. You may not use the same element (same index) twice.
// 4. If no two numbers sum up to the target, return string "Target not found".
//
// 💡 Examples:
// - findTarget([2, 7, 11, 15], 9)      => [0, 1]
// - findTarget([3, 2, 4, 5], 6)        => [1, 2]
// - findTarget([1, 3, 5, 6, 7, 8], 15) => [4, 5]
// - findTarget([1, 3, 5, 7], 14)       => "Target not found"
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
function findTarget(nums, target) {
  // TODO: Implement your solution here.
  // (This function will automatically reset once you pass all tests)
  return "Target not found";
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
    "function findTarget(nums, target) {",
    "  // TODO: Implement your solution here.",
    "  // (This function will automatically reset once you pass all tests)",
    '  return "Target not found";',
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
    { nums: [2, 7, 11, 15], target: 9, expected: [0, 1] },
    { nums: [3, 2, 4, 5], target: 6, expected: [1, 2] },
    { nums: [1, 3, 5, 6, 7, 8], target: 15, expected: [4, 5] },
    { nums: [1, 3, 5, 7], target: 14, expected: "Target not found" },
  ];

  console.log(`\n🧪 Testing your [findTarget] function...\n`);

  const pad = (str, len) => (str + " ".repeat(len)).slice(0, len);
  const fmt = (val) => (Array.isArray(val) ? `[${val.join(", ")}]` : val);

  const header = `${pad("Input Array", 20)} | ${pad("Target", 6)} | ${pad(
    "Expected",
    18
  )} | ${pad("Actual", 18)} | Status`;
  console.log(header);
  console.log("-".repeat(header.length));

  let allPass = true;

  testCases.forEach(({ nums, target, expected }) => {
    let result;
    try {
      result = findTarget(nums, target);
    } catch (e) {
      result = "Error";
    }

    // Simple JSON comparison for arrays
    const isMatch = JSON.stringify(result) === JSON.stringify(expected);
    const statusIcon = isMatch ? "✅ PASS" : "❌ FAIL";

    if (!isMatch) allPass = false;

    let numsStr = fmt(nums);
    if (numsStr.length > 18) numsStr = numsStr.slice(0, 15) + "...";

    console.log(
      `${pad(numsStr, 20)} | ${pad(String(target), 6)} | ${pad(
        fmt(expected),
        18
      )} | ${pad(fmt(result), 18)} | ${statusIcon}`
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
