import * as fs from "fs";

// ======================================================================
// 🧠 CHALLENGE: Character Battle
// ======================================================================
// Description:
// Given two strings representing your army and an opposing army, determine
// the outcome of the battle based on character strengths.
//
// 📋 Rules:
// 1. Comparison happens by index (character at index 0 battles character at index 0).
// 2. Strength values:
//    - 'a'-'z': 1-26
//    - 'A'-'Z': 27-52
//    - '0'-'9': Face value (0-9)
//    - Others: 0
// 3. Outcomes:
//    - If your army is larger: "Opponent retreated"
//    - If opponent army is larger: "We retreated"
//    - Otherwise, count battles won (stronger character wins, ties award no points).
//      - More wins: "We won"
//      - Fewer wins: "We lost"
//      - Equal wins: "It was a tie"
//
// 💡 Examples:
// - battle("Hello", "World") => "We lost"
// - battle("pizza", "salad") => "We won"
// - battle("kn!ght", "orc")  => "Opponent retreated"
// ======================================================================

// #region [📚 Reference Solutions]

function battle1(myArmy: string, opponentArmy: string): string {
  // 1. Length Check
  if (myArmy.length > opponentArmy.length) return "Opponent retreated";
  if (opponentArmy.length > myArmy.length) return "We retreated";

  let myWins = 0;
  let oppWins = 0;

  // 2. Battle Loop
  for (let i = 0; i < myArmy.length; i++) {
    const myStr = getStrength(myArmy.charCodeAt(i));
    const oppStr = getStrength(opponentArmy.charCodeAt(i));

    if (myStr > oppStr) myWins++;
    else if (oppStr > myStr) oppWins++;
  }

  // 3. Result
  if (myWins > oppWins) return "We won";
  if (oppWins > myWins) return "We lost";
  return "It was a tie";
}

/**
 * Helper to calculate strength based on character code rules
 */
function getStrength(code: number): number {
  if (code >= 65 && code <= 90) return code - 38; // A-Z (27-52)
  if (code >= 97 && code <= 122) return code - 96; // a-z (1-26)
  if (code >= 48 && code <= 57) return code - 48; // 0-9 (0-9)
  return 0;
}

// #endregion

// ======================================================================
//  #region [✍️ Practice Area]
//  Please write your solution between the markers below.
// ======================================================================
// <PRACTICE_START>
function battle(myArmy: string, opposingArmy: string): string {
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
    "function battle(myArmy: string, opposingArmy: string): string {",
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
  } catch (e: any) {
    console.log(`⚠️ Reset failed: ${e.message}`);
  }
}

type TestCase = {
  myArmy: string;
  opposingArmy: string;
  expected: string;
};

function runTests() {
  const testCases: TestCase[] = [
    { myArmy: "Hello", opposingArmy: "World", expected: "We lost" },
    { myArmy: "pizza", opposingArmy: "salad", expected: "We won" },
    { myArmy: "C@T5", opposingArmy: "D0G$", expected: "We won" },
    { myArmy: "kn!ght", opposingArmy: "orc", expected: "Opponent retreated" },
    { myArmy: "PC", opposingArmy: "Mac", expected: "We retreated" },
    { myArmy: "Wizards", opposingArmy: "Dragons", expected: "It was a tie" },
    {
      myArmy: "Mr. Smith",
      opposingArmy: "Dr. Jones",
      expected: "It was a tie",
    },
  ];

  console.log(`\n🧪 Testing your [battle] function...\n`);

  const pad = (str: string, len: number) =>
    (str + " ".repeat(len)).slice(0, len);

  const header = `${pad("My Army", 12)} | ${pad("Opponent", 12)} | ${pad(
    "Expected",
    18
  )} | ${pad("Actual", 18)} | Status`;
  console.log(header);
  console.log("-".repeat(header.length));

  let allPass = true;

  testCases.forEach(({ myArmy, opposingArmy, expected }) => {
    let result: any;
    try {
      result = battle(myArmy, opposingArmy);
    } catch (e) {
      result = "Error";
    }

    const isMatch = result === expected;
    const statusIcon = isMatch ? "✅ PASS" : "❌ FAIL";

    if (!isMatch) allPass = false;

    console.log(
      `${pad(myArmy, 12)} | ${pad(opposingArmy, 12)} | ${pad(
        expected,
        18
      )} | ${pad(String(result), 18)} | ${statusIcon}`
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
