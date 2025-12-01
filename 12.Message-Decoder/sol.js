const fs = require("fs");

// ======================================================================
// 🧠 CHALLENGE: Message Decoder
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
// - decode("Xlmw mw...", 4)  => "This is..." ('X' is 'T' shifted +4, so go back 4)
// - decode("Byffi...", 20)   => "Hello..."
// - decode("Zqd...", -1)     => "Are..."     (Encoded -1, so shift +1 to decode)
// ======================================================================

// #region [📚 Reference Solutions] (Solutions hidden as requested)
// (Focus on implementing your own logic in the Practice Area below!)
// #endregion

// ======================================================================
//  #region [✍️ Practice Area]
//  Please write your solution between the markers below.
// ======================================================================
// <PRACTICE_START>
function decode(message, shift) {
  // TODO: Implement your solution here.
  return "";
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
    "function decode(message, shift) {",
    "  // TODO: Implement your solution here.",
    '  return "";',
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
    {
      message: "Xlmw mw e wigvix qiwweki.",
      shift: 4,
      expected: "This is a secret message.",
    },
    { message: "Byffi Qilfx!", shift: 20, expected: "Hello World!" },
    { message: "Zqd xnt njzx?", shift: -1, expected: "Are you okay?" },
    { message: "oannLxmnLjvy", shift: 9, expected: "freeCodeCamp" },
  ];

  console.log(`\n🧪 Testing your [decode] function...\n`);

  const pad = (str, len) => (str + " ".repeat(len)).slice(0, len);

  const header = `${pad("Input Message", 20)} | ${pad("Shift", 6)} | ${pad(
    "Expected",
    20
  )} | ${pad("Actual", 20)} | Status`;
  console.log(header);
  console.log("-".repeat(header.length));

  let allPass = true;

  testCases.forEach(({ message, shift, expected }) => {
    let result;
    try {
      result = decode(message, shift);
    } catch (e) {
      result = "Error";
    }

    const isMatch = result === expected;
    const statusIcon = isMatch ? "✅ PASS" : "❌ FAIL";

    if (!isMatch) allPass = false;

    let msgStr = message.length > 18 ? message.slice(0, 15) + "..." : message;
    let expStr =
      expected.length > 18 ? expected.slice(0, 15) + "..." : expected;
    let resStr =
      String(result).length > 18
        ? String(result).slice(0, 15) + "..."
        : String(result);

    console.log(
      `${pad(msgStr, 20)} | ${pad(String(shift), 6)} | ${pad(
        expStr,
        20
      )} | ${pad(resStr, 20)} | ${statusIcon}`
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
