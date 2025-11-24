import os
import sys

# ======================================================================
# 🧠 CHALLENGE: Targeted Sum (Python Version)
# ======================================================================
# Description:
# Given an array of numbers and an integer target, find two unique numbers
# in the array that add up to the target value.
#
# 📋 Rules:
# 1. Return a list containing the INDICES of the two numbers.
# 2. The indices in the result must be in ascending order (e.g., [0, 1]).
# 3. You may not use the same element (same index) twice.
# 4. If no two numbers sum up to the target, return string "Target not found".
#
# 💡 Examples:
# - find_target([2, 7, 11, 15], 9)      => [0, 1]
# - find_target([3, 2, 4, 5], 6)        => [1, 2]
# - find_target([1, 3, 5, 6, 7, 8], 15) => [4, 5]
# - find_target([1, 3, 5, 7], 14)       => "Target not found"
# ======================================================================

# region [📚 Reference Solutions] (Solutions hidden as requested)

# (Reference solutions have been removed.)
# (Focus on implementing your own logic in the Practice Area below!)

# endregion


# ======================================================================
#  region [✍️ Practice Area]
#  Please write your solution between the markers below.
# ======================================================================
# <PRACTICE_START>
def find_target(nums, target):
    # TODO: Implement your solution here.
    # (This function will automatically reset once you pass all tests)
    return "Target not found"
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
        "def find_target(nums, target):\n",
        "    # TODO: Implement your solution here.\n",
        "    # (This function will automatically reset once you pass all tests)\n",
        '    return "Target not found"\n',
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
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4, 5], 6, [1, 2]),
        ([1, 3, 5, 6, 7, 8], 15, [4, 5]),
        ([1, 3, 5, 7], 14, "Target not found"),
    ]

    print(f"\n🧪 Testing your [find_target] function...\n")

    # Header
    header = f"{'Input Array':<20} | {'Target':<6} | {'Expected':<18} | {'Actual':<18} | Status"
    print(header)
    print("-" * len(header))

    all_pass = True
    for nums, target, expected in test_cases:
        try:
            result = find_target(nums, target)
        except Exception as e:
            result = "Error"

        # Check equality
        is_match = result == expected
        status_icon = "✅ PASS" if is_match else "❌ FAIL"
        if not is_match:
            all_pass = False

        # Formatting for display
        nums_str = str(nums)
        if len(nums_str) > 18:
            nums_str = nums_str[:15] + "..."

        print(
            f"{nums_str:<20} | {str(target):<6} | {str(expected):<18} | {str(result):<18} | {status_icon}"
        )

    print("-" * len(header))
    if all_pass:
        print("\n🎉 Fantastic! All test cases passed.")
        reset_practice_area()
    else:
        print("\n⚠️  Some tests failed. Keep trying! (The file will not reset yet)")

# endregion
