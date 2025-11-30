import os
import sys

# ======================================================================
# 🧠 CHALLENGE: 3 Strikes (Python Version)
# ======================================================================
# Description:
# Given an integer n (between 1 and 10,000), return a count of how many
# numbers from 1 up to n (inclusive) have a square that contains
# at least one digit '3'.
#
# 📋 Rules:
# 1. n will be an integer between 1 and 10,000.
# 2. Calculate the square of each number from 1 to n.
# 3. Check if the string representation of that square contains the character '3'.
# 4. Return the count of such numbers.
#
# 💡 Examples:
# - squares_with_three(1)   => 0   (1^2 = 1, no '3')
# - squares_with_three(10)  => 1   (Only 6^2 = 36 contains '3')
# - squares_with_three(100) => 19
# ======================================================================

# #region [📚 Reference Solutions]


def squares_with_three_math(n: int) -> int:
    """
    Method: Mathematical (Integer Division)
    Best for: Performance (no string allocation).
    Complexity: Time O(N) | Space O(1)
    """
    count = 0
    for i in range(1, n + 1):
        square = i * i

        while square > 0:
            if square % 10 == 3:
                count += 1
                break
            # Use // for integer floor division in Python
            square //= 10

    return count


# #endregion


# ======================================================================
#  region [✍️ Practice Area]
#  Please write your solution between the markers below.
# ======================================================================
# <PRACTICE_START>
def squares_with_three(n):
    # TODO: Implement your solution here.
    return 0
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
        "def squares_with_three(n):\n",
        "    # TODO: Implement your solution here.\n",
        "    return 0\n",
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
        (1, 0),
        (10, 1),
        (100, 19),
        (1000, 326),
        (10000, 4531),
    ]

    print(f"\n🧪 Testing your [squares_with_three] function...\n")

    header = f"{'Input (n)':<10} | {'Expected':<10} | {'Actual':<10} | Status"
    print(header)
    print("-" * len(header))

    all_pass = True
    for n, expected in test_cases:
        try:
            result = squares_with_three(n)
        except Exception as e:
            result = "Error"

        is_match = result == expected
        status_icon = "✅ PASS" if is_match else "❌ FAIL"
        if not is_match:
            all_pass = False

        print(f"{str(n):<10} | {str(expected):<10} | {str(result):<10} | {status_icon}")

    print("-" * len(header))
    if all_pass:
        print("\n🎉 Fantastic! All test cases passed.")
        reset_practice_area()
    else:
        print("\n⚠️  Some tests failed. Keep trying! (The file will not reset yet)")

# endregion
