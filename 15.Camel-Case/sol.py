import os
import re
import sys

# ======================================================================
# 🧠 CHALLENGE: camelCase (Python Version)
# ======================================================================
# Description:
# Given a string, return its camel case version using the following rules:
# 1. Words are separated by spaces ( ), dashes (-), or underscores (_).
# 2. Treat any sequence of these characters as a single word break.
# 3. The first word should be all lowercase.
# 4. Each subsequent word should start with an uppercase letter,
#    with the rest of it lowercase.
# 5. All spaces and separators should be removed.
#
# 💡 Examples:
# - to_camel_case("hello world")       => "helloWorld"
# - to_camel_case("HELLO WORLD")       => "helloWorld"
# - to_camel_case("secret agent-X")    => "secretAgentX"
# - to_camel_case("FREE cODE cAMP")    => "freeCodeCamp"
# ======================================================================


# region [📚 Reference Solutions] (Solutions hidden as requested)
def to_camel_case_simple(text):
    # Normalize separators to spaces, then split
    text = text.replace("-", " ").replace("_", " ")
    words = text.split()  # split() without args handles multiple spaces

    if not words:
        return ""

    # Logic: Lowercase first word + Title case rest
    first = words[0].lower()
    rest = [w.capitalize() for w in words[1:]]

    return first + "".join(rest)


# endregion


# ======================================================================
#  region [✍️ Practice Area]
#  Please write your solution between the markers below.
# ======================================================================
# <PRACTICE_START>
def to_camel_case(text):
    text = text.replace("-", " ").replace("_", " ")
    words = text.split()

    if not words:
        return ""

    first = words[0].lower()
    rest = [w.capitalize() for w in words[1:]]

    return first + "".join(rest)


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
        "def to_camel_case(text):\n",
        "    # TODO: Implement your solution here.\n",
        '    return ""\n',
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
        ("hello world", "helloWorld"),
        ("HELLO WORLD", "helloWorld"),
        ("secret agent-X", "secretAgentX"),
        ("FREE cODE cAMP", "freeCodeCamp"),
        (
            "ye old-_-sea  faring_buccaneer_-_with a - peg__leg----and a_parrot_ _named- _squawk",
            "yeOldSeaFaringBuccaneerWithAPegLegAndAParrotNamedSquawk",
        ),
    ]

    print(f"\n🧪 Testing your [to_camel_case] function...\n")

    header = f"{'Input String':<25} | {'Expected':<20} | {'Actual':<20} | Status"
    print(header)
    print("-" * len(header))

    all_pass = True
    for text, expected in test_cases:
        try:
            result = to_camel_case(text)
        except Exception as e:
            result = "Error"

        is_match = result == expected
        status_icon = "✅ PASS" if is_match else "❌ FAIL"
        if not is_match:
            all_pass = False

        # Helper to truncate
        def trunc(s, length):
            return s[: length - 3] + "..." if len(s) > length else s

        print(
            f"{trunc(text, 25):<25} | {trunc(expected, 20):<20} | {trunc(str(result), 20):<20} | {status_icon}"
        )

    print("-" * len(header))
    if all_pass:
        print("\n🎉 Fantastic! All test cases passed.")
        reset_practice_area()
    else:
        print("\n⚠️  Some tests failed. Keep trying! (The file will not reset yet)")

# endregion
