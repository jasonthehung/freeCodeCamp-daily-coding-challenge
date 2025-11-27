import math
import os
import sys

# ======================================================================
# 🧠 CHALLENGE: Mile Pace (Python Version)
# ======================================================================
# Description:
# Given a distance in miles (number) and a total time in "MM:SS" format,
# return the average pace per mile as a string in "MM:SS" format.
#
# 📋 Rules:
# 1. Return the average time it took to run each mile.
# 2. The output format must be "MM:SS".
# 3. Ensure leading zeros are added where needed (e.g., "04:36", not "4:36").
# 4. Round the seconds to the nearest whole number.
#
# 💡 Examples:
# - mile_pace(3, "24:00")     => "08:00"
# - mile_pace(1, "06:45")     => "06:45"
# - mile_pace(2, "07:00")     => "03:30"
# - mile_pace(26.2, "120:35") => "04:36"
# ======================================================================

# #region [📚 Reference Solutions]


def mile_pace1(distance: float, time_str: str) -> str:
    """
    Method: Arithmetic & String Formatting
    Note: Python's `divmod` and f-string padding `:02d` make this very concise.
    """
    # 1. Parse input
    minutes, seconds = map(int, time_str.split(":"))

    # 2. Convert to total seconds
    total_seconds = (minutes * 60) + seconds

    # 3. Calculate pace per mile (round to nearest integer)
    pace_seconds = round(total_seconds / distance)

    # 4. Convert back to (min, sec) using divmod
    # divmod(200, 60) -> returns (3, 20)
    m, s = divmod(pace_seconds, 60)

    # 5. Format: :02d ensures 2 digits with leading zero
    return f"{m:02d}:{s:02d}"


# #endregion


# ======================================================================
#  region [✍️ Practice Area]
#  Please write your solution between the markers below.
# ======================================================================
# <PRACTICE_START>
def mile_pace(miles, time):
    min, sec = map(int, time.split(":"))

    total_sec = min * 60 + sec

    pace_sec = round(total_sec / miles)

    mm, ss = divmod(pace_sec, 60)

    return f"{mm:02d}:{ss:02d}"


# <PRACTICE_END>
# endregion

# ======================================================================
#  region [🚀 Test Runner & Auto-Reset] (Do not modify below this line)
# ======================================================================


def reset_practice_area():
    print("\n🔄 Resetting Practice Area to default state...")
    MARKER_START = "# <PRACTICE_" + "START>"
    MARKER_END = "# <PRACTICE_" + "END>"

    default_code_lines = [
        "def mile_pace(miles, time):\n",
        "    # TODO: Implement your solution here.\n",
        '    return "00:00"\n',
    ]

    try:
        current_file = __file__
        with open(current_file, "r", encoding="utf-8") as f:
            lines = f.readlines()

        start_idx = -1
        end_idx = -1

        for i, line in enumerate(lines):
            if MARKER_START in line:
                start_idx = i
            if MARKER_END in line:
                end_idx = i

        if start_idx == -1 or end_idx == -1 or start_idx >= end_idx:
            print("⚠️ Error: Markers not found. Reset cancelled.")
            return

        new_content = lines[: start_idx + 1] + default_code_lines + lines[end_idx:]

        with open(current_file, "w", encoding="utf-8") as f:
            f.writelines(new_content)
        print("✨ Reset complete! The file is ready for a fresh start.")
    except Exception as e:
        print(f"⚠️ Reset failed: {e}")


if __name__ == "__main__":
    test_cases = [
        (3, "24:00", "08:00"),
        (1, "06:45", "06:45"),
        (2, "07:00", "03:30"),
        (26.2, "120:35", "04:36"),
    ]

    print(f"\n🧪 Testing your [mile_pace] function...\n")

    header = f"{'Miles':<8} | {'Time':<8} | {'Expected':<10} | {'Actual':<10} | Status"
    print(header)
    print("-" * len(header))

    all_pass = True
    for miles, time, expected in test_cases:
        try:
            result = mile_pace(miles, time)
        except Exception as e:
            result = "Error"

        is_match = result == expected
        status_icon = "✅ PASS" if is_match else "❌ FAIL"
        if not is_match:
            all_pass = False

        print(
            f"{str(miles):<8} | {time:<8} | {expected:<10} | {str(result):<10} | {status_icon}"
        )

    print("-" * len(header))
    if all_pass:
        print("\n🎉 Fantastic! All test cases passed.")
        reset_practice_area()
    else:
        print("\n⚠️  Some tests failed. Keep trying! (The file will not reset yet)")

# endregion
