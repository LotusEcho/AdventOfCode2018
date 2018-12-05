import os
import string
import sys
from datetime import datetime

start_time = datetime.now()
sys.setrecursionlimit(1900)  # I live dangerously


def react(reaction_subset, reaction_string):
    original_string_len = len(reaction_string)
    new_string = reaction_string
    for character in reaction_subset:
        new_string = new_string.replace(f"{character}{character.upper()}", "")
        new_string = new_string.replace(f"{character.upper()}{character}", "")

    if len(new_string) == 0 or len(new_string) == original_string_len:
        return new_string
    else:
        return react(reaction_subset, new_string)


def remove_chain(reaction_string):

    smallest_string = reaction_string
    for character in string.ascii_lowercase:
        new_string = reaction_string.replace(f"{character}", "").replace(f"{character.upper()}", "")
        reacted_string = react(string.ascii_lowercase.replace(character, ""), new_string)
        if len(reacted_string) < len(smallest_string):
            smallest_string = reacted_string
    return smallest_string


input_file = open(os.path.join(os.path.dirname(__file__), 'day5_input.txt'), 'r')
input_text = input_file.readline().strip()
print(f"Original polymer length: {len (input_text)}")

answer = remove_chain(input_text)
print(f"The remaining polymer is {len(answer)} units long. Polymer: {answer}")
print(f"Run time: {datetime.now() - start_time}")
