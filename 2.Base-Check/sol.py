import re

# ======================================================================
# 🧠 CHALLENGE: Base Check
# ======================================================================
# Description:
# Given a string representing a number (n) and an integer base (from 2 to 36),
# determine whether the number is valid in that specific base.
#
# 📋 Rules:
# 1. The string 'n' may contain integers (0-9) and letters (A-Z).
# 2. The validation must be case-insensitive ('a' == 'A').
# 3. The 'base' will be an integer between 2 and 36.
# 4. Return True if valid, False otherwise.
#
# 💡 Examples of Valid Digits:
# - Base 2:  0, 1
# - Base 10: 0-9
# - Base 16: 0-9, A-F
# - Base 36: 0-9, A-Z
# ======================================================================

DIGITS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# region [📚 Reference Solutions] (Fold this region to hide answers)


def solution_1_regex(n, base):
    """
    Method 1: Regular Expressions
    -------------------------------------------------
    Best for: Defining complex string patterns compactly.
    Pros: Very concise code; declarative logic.
    Cons: Can be slower for very long strings; requires Regex knowledge.
    """
    if not (2 <= base <= 36):
        return False

    # Create the pool of allowed characters (Slicing)
    allowed = DIGITS[:base]

    # Construct the Regex Pattern
    # ^     : Start of string
    # [...] : Character set (any char inside is valid)
    # +     : One or more occurrences
    # $     : End of string
    pattern = f"^[{allowed}]+$"

    # re.IGNORECASE matches 'a' and 'A' equally
    return re.fullmatch(pattern, n, re.IGNORECASE) is not None


def solution_2_loop(n, base):
    """
    Method 2: Algorithmic Lookup (★ Recommended for Interviews)
    -------------------------------------------------
    Best for: Demonstrating understanding of data structures (Sets).
    Pros: High performance (O(N)); logic is transferable to C++/Java.
    """
    if not (2 <= base <= 36):
        return False

    # Using a 'set' is crucial here because checking "x in set" is O(1),
    # whereas checking "x in list" is O(N).
    allowed = set(DIGITS[:base])

    for char in n.upper():
        # Early Exit: If we find ONE invalid character, fail immediately.
        if char not in allowed:
            return False

    return True


def solution_3_pythonic(n, base):
    """
    Method 3: Pythonic Built-in (★ Fastest in Practice)
    -------------------------------------------------
    Best for: Real-world Python development.
    Pros: Extremely fast (C-optimized); shortest code.
    Cons: Relies on Exception handling for control flow.
    """
    if not (2 <= base <= 36):
        return False

    try:
        # int(string, base) attempts to parse the string.
        # It raises ValueError if the string contains invalid digits.
        int(n, base)
        return True
    except ValueError:
        return False


# endregion


# ======================================================================
#  ✍️ [Practice Area]
#  Please write your solution between the <START> and <END> tags.
# ======================================================================
# <PRACTICE_START>
def is_valid_number(n, base):
    # TODO: Implement your solution here.
    # (This function will automatically reset once you pass all tests)
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
    # We split the strings to prevent this script from finding itself.
    MARKER_START = "# <PRACTICE_" + "START>"
    MARKER_END = "# <PRACTICE_" + "END>"

    # 2. Define Default Code (The "Blank Slate")
    default_code_lines = [
        "def is_valid_number(n, base):\n",
        "    # TODO: Implement your solution here.\n",
        "    # (This function will automatically reset once you pass all tests)\n",
        "    return False\n",
    ]

    try:
        # 3. Read the current file
        current_file = __file__
        with open(current_file, "r", encoding="utf-8") as f:
            lines = f.readlines()

        # 4. Locate the Practice Area
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
            print("⚠️ Error: Invalid marker order (Start >= End). Reset cancelled.")
            return

        # 6. Reconstruct the File
        # [Header ... Start Marker] + [Default Code] + [End Marker ... Footer]
        new_content = lines[: start_idx + 1] + default_code_lines + lines[end_idx:]

        # 7. Overwrite the file
        with open(current_file, "w", encoding="utf-8") as f:
            f.writelines(new_content)

        print("✨ Reset complete! The file is ready for a fresh start.")

    except Exception as e:
        print(f"⚠️ Reset failed: {e}")


if __name__ == "__main__":
    # Test Cases: (Input String, Base, Expected Result)
    test_cases = [
        ("10101", 2, True),
        ("10201", 2, False),  # '2' is invalid in base 2
        ("76543210", 8, True),
        ("9876543210", 8, False),  # '9', '8' invalid in base 8
        ("9876543210", 10, True),
        ("ABC", 10, False),  # Letters invalid in base 10
        ("ABC", 16, True),
        ("Z", 36, True),
        ("ABC", 20, True),
        ("4B4BA9", 16, True),
        ("5G3F8F", 16, False),  # 'G' is invalid in base 16
        ("5G3F8F", 17, True),  # 'G' is valid in base 17
        ("abc", 10, False),
        ("abc", 16, True),  # Lowercase check
        ("AbC", 16, True),  # Mixed case check
        ("z", 36, True),
    ]

    print(f"\n🧪 Testing your [is_valid_number] function...\n")

    # Table Header
    header = f"{'Input':<12} | {'Base':<6} | {'Expected':<8} | {'Actual':<8} | Status"
    print(header)
    print("-" * len(header))

    all_pass = True

    for n, base, expected in test_cases:
        try:
            result = is_valid_number(n, base)
        except Exception as e:
            result = "Error"

        # Visual formatting
        status_icon = "✅ PASS" if result == expected else "❌ FAIL"
        if result != expected:
            all_pass = False

        print(
            f"{n:<12} | {base:<6} | {str(expected):<8} | {str(result):<8} | {status_icon}"
        )

    print("-" * len(header))

    if all_pass:
        print("\n🎉 Fantastic! All test cases passed.")
        reset_practice_area()
    else:
        print("\n⚠️  Some tests failed. Keep trying! (The file will not reset yet)")
# endregion
