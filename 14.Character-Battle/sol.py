import os
import sys

# ======================================================================
# 🧠 CHALLENGE: Character Battle (Python Version)
# ======================================================================
# Description:
# Given two strings representing your army and an opposing army, determine
# the outcome of the battle based on character strengths.
#
# 📋 Rules:
# 1. Comparison happens by index (character at index 0 battles character at index 0).
# 2. Strength values:
#    - 'a'-'z': 1-26
#    - 'A'-'Z': 27-52
#    - '0'-'9': Face value (0-9)
#    - Others: 0
# 3. Outcomes:
#    - If len(my_army) > len(opposing_army): "Opponent retreated"
#    - If len(opposing_army) > len(my_army): "We retreated"
#    - Otherwise, count battles won (stronger character wins, ties award no points).
#      - More wins: "We won"
#      - Fewer wins: "We lost"
#      - Equal wins: "It was a tie"
#
# 💡 Examples:
# - battle("Hello", "World") => "We lost"
# - battle("pizza", "salad") => "We won"
# - battle("kn!ght", "orc")  => "Opponent retreated"
# ======================================================================


# #region [📚 Reference Solutions]


def get_strength(char: str) -> int:
    """Helper to map characters to strength values"""
    if "A" <= char <= "Z":
        return ord(char) - 38
    elif "a" <= char <= "z":
        return ord(char) - 96
    elif "0" <= char <= "9":
        return ord(char) - 48
    return 0


def battle1(my_army: str, opponent_army: str) -> str:
    """
    Method: Linear Scan
    Complexity: Time O(N) | Space O(1)
    """
    # 1. Length Check
    if len(my_army) > len(opponent_army):
        return "Opponent retreated"
    if len(opponent_army) > len(my_army):
        return "We retreated"

    my_wins = 0
    opp_wins = 0

    # 2. Battle Loop
    # zip() allows us to iterate both strings simultaneously
    for c1, c2 in zip(my_army, opponent_army):
        s1 = get_strength(c1)
        s2 = get_strength(c2)

        if s1 > s2:
            my_wins += 1
        elif s2 > s1:
            opp_wins += 1

    # 3. Result
    if my_wins > opp_wins:
        return "We won"
    elif opp_wins > my_wins:
        return "We lost"
    else:
        return "It was a tie"


# #endregion


# ======================================================================
#  region [✍️ Practice Area]
#  Please write your solution between the markers below.
# ======================================================================
# <PRACTICE_START>
def battle(my_army, opposing_army):
    # TODO: Implement your solution here.
    return ""


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
        "def battle(my_army, opposing_army):\n",
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
        ("Hello", "World", "We lost"),
        ("pizza", "salad", "We won"),
        ("C@T5", "D0G$", "We won"),
        ("kn!ght", "orc", "Opponent retreated"),
        ("PC", "Mac", "We retreated"),
        ("Wizards", "Dragons", "It was a tie"),
        ("Mr. Smith", "Dr. Jones", "It was a tie"),
    ]

    print(f"\n🧪 Testing your [battle] function...\n")

    header = f"{'My Army':<12} | {'Opponent':<12} | {'Expected':<18} | {'Actual':<18} | Status"
    print(header)
    print("-" * len(header))

    all_pass = True
    for my_army, opposing_army, expected in test_cases:
        try:
            result = battle(my_army, opposing_army)
        except Exception as e:
            result = "Error"

        is_match = result == expected
        status_icon = "✅ PASS" if is_match else "❌ FAIL"
        if not is_match:
            all_pass = False

        my_str = my_army if len(my_army) <= 12 else my_army[:9] + "..."
        op_str = (
            opposing_army if len(opposing_army) <= 12 else opposing_army[:9] + "..."
        )

        print(
            f"{my_str:<12} | {op_str:<12} | {expected:<18} | {str(result):<18} | {status_icon}"
        )

    print("-" * len(header))
    if all_pass:
        print("\n🎉 Fantastic! All test cases passed.")
        reset_practice_area()
    else:
        print("\n⚠️  Some tests failed. Keep trying! (The file will not reset yet)")

# endregion
