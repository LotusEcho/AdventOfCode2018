from collections import defaultdict
from helper.input_output import file
import os


def count_twos_and_threes(input_string, **kwargs):
    """Iterates through a string and gets a count of every character in it.
    It then counts whether any of those characters are repeated 2 or 3 times.
    :param input_string: The string to iterate through.
    :param kwargs:
    :return: A dictionary containing whether it had a character repeated 2 times or 3 times (both can
        IE: {2: 1, 3: 1} if at least one character was repeated EXACTLY 2 times and another character repeated EXACTLY 3 times.
        IE: {2: 0, 3: 1} if no characters repeated EXACTLY 2 times but at least one character repeated EXACTLY 3 times.
    """
    character_dict = defaultdict(int)
    twos_and_threes = {2 : 0, 3 : 0}
    for character in input_string:
        character_dict[character] += 1
    for key in character_dict.keys():
        if twos_and_threes.get(2) == 1 and twos_and_threes.get(3) == 1:
            break  # If we already found a 2 and 3 character match don't check anymore.
        if character_dict.get(key) == 2:
            twos_and_threes[2] = 1
        if character_dict.get(key) == 3:
            twos_and_threes[3] = 1
    kwargs["count"][2] += twos_and_threes.get(2)
    kwargs["count"][3] += twos_and_threes.get(3)
    return twos_and_threes


# Initialize stuff we'll use both in tests and in solving code
current_counts = {2 : 0, 3 : 0}
args = {"count": current_counts}

# Test cases to make sure we're getting the values we want before using it on the checksum
test_none = {2 : 0, 3 : 0}
assert(count_twos_and_threes("abcdefgggg", **args) == test_none)
test_two = {2 : 1, 3 : 0}
assert(count_twos_and_threes("aabcdefg", **args) == test_two)
test_three = {2 : 0, 3 : 1}
assert(count_twos_and_threes("abbbcdefggggggg", **args) == test_three)
test_both = {2 : 1, 3 : 1}
assert(count_twos_and_threes("abcccdeffg", **args) == test_both)
assert(current_counts[2] == 2)
assert(current_counts[3] == 2)

# Done testing, now for the solving!
current_counts = {2 : 0, 3 : 0} # Reset time
args = {"count": current_counts}
filename = os.path.join(os.path.dirname(__file__), 'day2_input.txt')

line_list, answer_list = file.load_file_iterative_function(filename, count_twos_and_threes, **args)
print(f"Of the {len(line_list)} lines of input we got {len(answer_list)} answers and found {current_counts[2]} number of strings with a "
      f"character that was repeated EXACTLY 2 times and {current_counts[3]} number of strings with a character that "
      f"was repeated EXACTLY 3 times.")
print(f"This gives us a list checksum of {current_counts[2] * current_counts[3]}")
