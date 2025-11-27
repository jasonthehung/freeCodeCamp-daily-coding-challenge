const fs = require("fs");

// ======================================================================
// 🧠 CHALLENGE: Mile Pace
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
// - milePace(3, "24:00")     => "08:00"
// - milePace(1, "06:45")     => "06:45"
// - milePace(2, "07:00")     => "03:30"
// - milePace(26.2, "120:35") => "04:36"
// ======================================================================

// #region [📚 Reference Solutions]

/**
 * Method: Arithmetic Conversion
 * Logic: Convert "MM:SS" -> Total Seconds -> Divide -> Reformat.
 */
function milePace(distance, time) {
  const [minStr, secStr] = time.split(":");

  // Calculate total seconds
  const totalSeconds = parseInt(minStr) * 60 + parseInt(secStr);

  // Calculate pace in seconds and round to nearest whole number
  const paceInSeconds = Math.round(totalSeconds / distance);

  // Convert back to minutes and seconds
  const paceMin = Math.floor(paceInSeconds / 60);
  const paceSec = paceInSeconds % 60;

  // Format with leading zeros (e.g., "3" -> "03")
  return `${String(paceMin).padStart(2, "0")}:${String(paceSec).padStart(
    2,
    "0"
  )}`;
}

// #endregion

// ======================================================================
//  #region [✍️ Practice Area]
//  Please write your solution between the markers below.
// ======================================================================
// <PRACTICE_START>
function milePace(miles, time) {
  // TODO: Implement your solution here.
  return "00:00";
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
    "function milePace(miles, time) {",
    "  // TODO: Implement your solution here.",
    '  return "00:00";',
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
    { miles: 3, time: "24:00", expected: "08:00" },
    { miles: 1, time: "06:45", expected: "06:45" },
    { miles: 2, time: "07:00", expected: "03:30" },
    { miles: 26.2, time: "120:35", expected: "04:36" },
  ];

  console.log(`\n🧪 Testing your [milePace] function...\n`);

  const pad = (str, len) => (str + " ".repeat(len)).slice(0, len);

  const header = `${pad("Miles", 8)} | ${pad("Time", 8)} | ${pad(
    "Expected",
    10
  )} | ${pad("Actual", 10)} | Status`;
  console.log(header);
  console.log("-".repeat(header.length));

  let allPass = true;

  testCases.forEach(({ miles, time, expected }) => {
    let result;
    try {
      result = milePace(miles, time);
    } catch (e) {
      result = "Error";
    }

    const isMatch = result === expected;
    const statusIcon = isMatch ? "✅ PASS" : "❌ FAIL";

    if (!isMatch) allPass = false;

    console.log(
      `${pad(String(miles), 8)} | ${pad(time, 8)} | ${pad(
        expected,
        10
      )} | ${pad(String(result), 10)} | ${statusIcon}`
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
