import os
import sys

# ======================================================================
# 🧠 CHALLENGE: Factorializer (Python Version)
# ======================================================================
# Description:
# Given an integer n (from 0 to 20), return the factorial of that number.
# The factorial of a number is the product of all positive integers
# less than or equal to n.
#
# 📋 Rules:
# 1. n will be an integer between 0 and 20.
# 2. factorial(0) is defined as 1.
# 3. Return the calculated factorial value.
#
# 💡 Examples:
# - factorial(0)  => 1
# - factorial(5)  => 120  (5 * 4 * 3 * 2 * 1)
# - factorial(20) => 2432902008176640000
# ======================================================================

# region [📚 Reference Solutions] (Solutions hidden as requested)


def sum_of_squares_iterative(n: int) -> int:
    """
    Method 1: Generator Expression (Pythonic)
    Best for: Readability and concise code.
    Complexity: Time O(n)
    """
    return sum(i * i for i in range(1, n + 1))


def sum_of_squares_math(n: int) -> int:
    """
    Method 2: Mathematical Formula (Optimal)
    Best for: High performance (O(1)) or large numbers.
    Formula: n(n + 1)(2n + 1) / 6
    Note: Uses // for integer division.
    """
    return (n * (n + 1) * (2 * n + 1)) // 6


# endregion


# ======================================================================
#  region [✍️ Practice Area]
#  Please write your solution between the markers below.
# ======================================================================
# <PRACTICE_START>
def factorial(n):
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
        "def factorial(n):\n",
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
        (0, 1),
        (1, 1),
        (5, 120),
        (10, 3628800),
        (20, 2432902008176640000),
    ]

    print(f"\n🧪 Testing your [factorial] function...\n")

    header = f"{'Input (n)':<10} | {'Expected':<20} | {'Actual':<20} | Status"
    print(header)
    print("-" * len(header))

    all_pass = True
    for n, expected in test_cases:
        try:
            result = factorial(n)
        except Exception as e:
            result = "Error"

        is_match = result == expected
        status_icon = "✅ PASS" if is_match else "❌ FAIL"
        if not is_match:
            all_pass = False

        print(f"{str(n):<10} | {str(expected):<20} | {str(result):<20} | {status_icon}")

    print("-" * len(header))
    if all_pass:
        print("\n🎉 Fantastic! All test cases passed.")
        reset_practice_area()
    else:
        print("\n⚠️  Some tests failed. Keep trying! (The file will not reset yet)")

# endregion
