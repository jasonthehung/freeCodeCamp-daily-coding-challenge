import sys

# ======================================================================
# 🧠 CHALLENGE: Vowel Balance
# ======================================================================
# Description:
# Given a string, determine whether the number of vowels in the first half
# of the string is equal to the number of vowels in the second half.
#
# 📋 Rules:
# 1. The string can contain any characters.
# 2. The letters a, e, i, o, and u, in either uppercase or lowercase,
#    are considered vowels.
# 3. If there's an odd number of characters in the string, ignore the
#    center character.
#
# 💡 Examples:
# - "racecar" -> 'rac' (1) vs 'car' (1) -> True
# - "string"  -> 'str' (0) vs 'ing' (1) -> False
# ======================================================================

# region [📚 Reference Solutions] (Fold this region to hide answers)


def solution_1_iterative(s):
    """
    Method 1: Iterative (Two Pointers)
    -------------------------------------------------
    Best for: Efficiency (Single Pass).
    Pros: O(N) time complexity.
    """
    # Define vowels locally for self-containment
    vowels = set("aeiouAEIOU")

    n = len(s)
    half = n // 2
    balance = 0

    for i in range(half):
        # Check character in the first half
        if s[i] in vowels:
            balance += 1

        # Check corresponding character in the second half
        # (n - 1 - i) gets the mirror index from the end
        if s[n - 1 - i] in vowels:
            balance -= 1

    return balance == 0


# endregion


# ======================================================================
#  ✍️ [Practice Area]
#  Please write your solution between the <START> and <END> tags.
# ======================================================================
# <PRACTICE_START>
def is_balanced(s):

    return False


# <PRACTICE_END>


# ======================================================================
#  🚀 [Test Runner & Auto-Reset] (Do not modify below this line)
# ======================================================================
# region Test Logic & Reset Script
def reset_practice_area():
    """
    Reads this file and restores the Practice Area to its default state
    only when all tests are passed.
    """
    print("\n🔄 Resetting Practice Area to default state...")

    # 1. Define Markers
    MARKER_START = "# <PRACTICE_" + "START>"
    MARKER_END = "# <PRACTICE_" + "END>"

    # 2. Define Default Code
    default_code_lines = [
        "def is_balanced(s):\n",
        "    # TODO: Implement your solution here.\n",
        "    # (This function will automatically reset once you pass all tests)\n",
        "    return False\n",
    ]

    try:
        # 3. Read current file
        current_file = __file__
        with open(current_file, "r", encoding="utf-8") as f:
            lines = f.readlines()

        # 4. Locate markers
        start_idx = -1
        end_idx = -1

        for i, line in enumerate(lines):
            if MARKER_START in line:
                start_idx = i
            elif MARKER_END in line:
                end_idx = i

        # 5. Safety Checks
        if start_idx == -1 or end_idx == -1:
            print("⚠️ Error: Markers not found. Reset cancelled.")
            return

        if start_idx >= end_idx:
            print("⚠️ Error: Invalid marker order. Reset cancelled.")
            return

        # 6. Reconstruct file
        new_content = lines[: start_idx + 1] + default_code_lines + lines[end_idx:]

        # 7. Write back
        with open(current_file, "w", encoding="utf-8") as f:
            f.writelines(new_content)

        print("✨ Reset complete! Ready for a fresh start.")

    except Exception as e:
        print(f"⚠️ Reset failed: {e}")


if __name__ == "__main__":
    # Test Cases: (Input String, Expected Result)
    test_cases = [
        ("racecar", True),  # rac(1) vs car(1)
        ("Lorem Ipsum", True),  # Lorem(2) vs Ipsum(2) - mid space ignored
        ("Kitty Ipsum", False),  # Kitty(1) vs Ipsum(2)
        ("string", False),  # str(0) vs ing(1)
        (" ", True),  # ""(0) vs ""(0)
        ("abcdefghijklmnopqrstuvwxyz", False),  # a-m(3) vs n-z(2)
        ("123A#b!E&*456-o.U", True),  # A,E(2) vs o,U(2)
    ]

    print(f"\n🧪 Testing your [is_balanced] function...\n")

    header = f"{'Input':<28} | {'Expected':<8} | {'Actual':<8} | Status"
    print(header)
    print("-" * len(header))

    all_pass = True

    for s, expected in test_cases:
        try:
            result = is_balanced(s)
        except Exception as e:
            result = "Error"

        status_icon = "✅ PASS" if result == expected else "❌ FAIL"
        if result != expected:
            all_pass = False

        # Format the input string to handle long strings in display
        display_s = (s[:25] + "..") if len(s) > 27 else s

        print(
            f"{display_s:<28} | {str(expected):<8} | {str(result):<8} | {status_icon}"
        )

    print("-" * len(header))

    if all_pass:
        print("\n🎉 Fantastic! All test cases passed.")
        reset_practice_area()
    else:
        print("\n⚠️  Some tests failed. Keep trying!")
# endregion
