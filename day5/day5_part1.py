import os
import string
from datetime import datetime

start_time = datetime.now()


def react(reaction_string):
    original_string_len = len(reaction_string)

    new_string = reaction_string.strip()
    for character in string.ascii_lowercase:
        new_string = new_string.replace(f"{character}{character.upper()}", "")
        new_string = new_string.replace(f"{character.upper()}{character}", "")

    if len(new_string) == original_string_len:
        return new_string
    else:
        return react(new_string)


input_file = open(os.path.join(os.path.dirname(__file__), 'day5_input.txt'), 'r')
input_text = input_file.readline()
print(f"Original polymer length: {len (input_text)}")

answer = react(input_text)
print(f"The remaining polymer is {len(answer)} units long. Polymer: {answer}")
print(f"Run time: {datetime.now() - start_time}")
