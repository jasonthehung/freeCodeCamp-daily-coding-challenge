import math
import os
import sys

# ======================================================================
# 🧠 CHALLENGE: Unnatural Prime (Python Version)
# ======================================================================
# Description:
# Given an integer, determine if that number is a prime number or a
# negative prime number.
#
# 📋 Rules:
# 1. A prime number is a positive integer greater than 1 that is only
#    divisible by 1 and itself.
# 2. A negative prime number is the negative version of a positive prime.
# 3. 0, 1, and -1 are NOT considered prime numbers.
# 4. Return True if the number is an "unnatural prime", False otherwise.
#
# 💡 Examples:
# - is_unnatural_prime(19)   => True
# - is_unnatural_prime(-23)  => True  (23 is prime)
# - is_unnatural_prime(1)    => False
# - is_unnatural_prime(0)    => False
# - is_unnatural_prime(-44)  => False
# ======================================================================

# region [📚 Reference Solutions] (Solutions hidden as requested)
# (Focus on implementing your own logic in the Practice Area below!)
# endregion


# ======================================================================
#  region [✍️ Practice Area]
#  Please write your solution between the markers below.
# ======================================================================
# <PRACTICE_START>
def is_unnatural_prime(n):
    # TODO: Implement your solution here.
    return False


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
        "def is_unnatural_prime(n):\n",
        "    # TODO: Implement your solution here.\n",
        "    return False\n",
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
        (1, False),
        (-1, False),
        (19, True),
        (-23, True),
        (0, False),
        (97, True),
        (-61, True),
        (99, False),
        (-44, False),
    ]

    print(f"\n🧪 Testing your [is_unnatural_prime] function...\n")

    header = f"{'Input':<8} | {'Expected':<10} | {'Actual':<10} | Status"
    print(header)
    print("-" * len(header))

    all_pass = True
    for n, expected in test_cases:
        try:
            result = is_unnatural_prime(n)
        except Exception as e:
            result = "Error"

        is_match = result == expected
        status_icon = "✅ PASS" if is_match else "❌ FAIL"
        if not is_match:
            all_pass = False

        print(f"{str(n):<8} | {str(expected):<10} | {str(result):<10} | {status_icon}")

    print("-" * len(header))
    if all_pass:
        print("\n🎉 Fantastic! All test cases passed.")
        reset_practice_area()
    else:
        print("\n⚠️  Some tests failed. Keep trying! (The file will not reset yet)")

# endregion
