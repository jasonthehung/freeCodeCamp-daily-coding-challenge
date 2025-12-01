import os
import sys

# ======================================================================
# 🧠 CHALLENGE: Message Decoder (Python Version)
# ======================================================================
# Description:
# Given a secret message string and an integer representing the shift amount
# used to encode it, return the decoded string.
#
# 📋 Rules:
# 1. The `shift` value represents how many positions letters were moved
#    to ENCODE the message. (e.g., shift 1 means A -> B).
# 2. To DECODE, you must shift in the opposite direction.
# 3. Positive shift = Encoded forward. Negative shift = Encoded backward.
# 4. Preserve case (Upper/Lower) and non-alphabetical characters.
# 5. Handle wrapping (A -> Z, Z -> A).
#
# 💡 Examples:
# - decode("Xlmw mw...", 4)  => "This is..." ('X' is 'T' shifted +4, so go back 4)
# - decode("Byffi...", 20)   => "Hello..."
# - decode("Zqd...", -1)     => "Are..."     (Encoded -1, so shift +1 to decode)
# ======================================================================

# region [📚 Reference Solutions] (Solutions hidden as requested)
# (Focus on implementing your own logic in the Practice Area below!)
# endregion


# ======================================================================
#  region [✍️ Practice Area]
#  Please write your solution between the markers below.
# ======================================================================
# <PRACTICE_START>
def decode(message: str, shift: int) -> str:
    """
    Method: List Comprehension & Ordinal Math
    Note: Python's % operator handles negative numbers mathematically correctly
    (e.g., -1 % 26 == 25), so the logic is slightly simpler than JS/Go.
    """
    result = []

    for char in message:
        if char.isalpha():
            # Determine base (65 for 'A', 97 for 'a')
            base = ord("A") if char.isupper() else ord("a")

            # 1. Convert char to 0-25 range: ord(char) - base
            # 2. Subtract shift to decode
            # 3. Modulo 26 handles the wrapping
            decoded_char = chr((ord(char) - base - shift) % 26 + base)
            result.append(decoded_char)
        else:
            result.append(char)

    return "".join(result)


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
        "def decode(message, shift):\n",
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
        ("Xlmw mw e wigvix qiwweki.", 4, "This is a secret message."),
        ("Byffi Qilfx!", 20, "Hello World!"),
        ("Zqd xnt njzx?", -1, "Are you okay?"),
        ("oannLxmnLjvy", 9, "freeCodeCamp"),
    ]

    print(f"\n🧪 Testing your [decode] function...\n")

    header = f"{'Input Message':<20} | {'Shift':<6} | {'Expected':<20} | {'Actual':<20} | Status"
    print(header)
    print("-" * len(header))

    all_pass = True
    for message, shift, expected in test_cases:
        try:
            result = decode(message, shift)
        except Exception as e:
            result = "Error"

        is_match = result == expected
        status_icon = "✅ PASS" if is_match else "❌ FAIL"
        if not is_match:
            all_pass = False

        msg_str = message[:15] + "..." if len(message) > 18 else message
        exp_str = expected[:15] + "..." if len(expected) > 18 else expected
        res_str = str(result)[:15] + "..." if len(str(result)) > 18 else str(result)

        print(
            f"{msg_str:<20} | {str(shift):<6} | {exp_str:<20} | {res_str:<20} | {status_icon}"
        )

    print("-" * len(header))
    if all_pass:
        print("\n🎉 Fantastic! All test cases passed.")
        reset_practice_area()
    else:
        print("\n⚠️  Some tests failed. Keep trying! (The file will not reset yet)")

# endregion
