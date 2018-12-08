import os
from helper.input_output import file


def compare_strings_in_list(list_of_strings):
    """Compares the list of strings recursively, failing fast when it finds more than 1 non-matching character.

    :param list_of_strings: The list of strings to iterate through, which gets smaller by one with each loop.
    :return: The two strings that match.

    ---------------------------------------------------------------------------------------------

    >>> compare_strings_in_list(["abcde", "fghij", "klmno", "pqrst", "fguij", "axcye", "wvxyz"])
    ('fghij', 'fguij')
    >>> compare_strings_in_list(["", "", "", "", "", ""])
    >>> compare_strings_in_list(["abcsdad", "abbsfdsf", "sdafjga"])
    Traceback (most recent call last):
    ...
    ValueError: The two strings had different lengths
    >>> compare_strings_in_list(["teststring", "teststring"])
    ('teststring', 'teststring')
    >>>
    """
    if len(list_of_strings) > 1:
        string_to_compare = list_of_strings.pop(0)
        if len(string_to_compare) > 0:
            for other_string in list_of_strings:
                if len(other_string) > 0:
                    diff_count = 0
                    if len(string_to_compare) != len(other_string):
                        raise ValueError("The two strings had different lengths")
                    for index in range(0, len(string_to_compare)):
                        if string_to_compare[index] != other_string[index]:
                            diff_count += 1
                        if diff_count > 1:
                            break
                    if diff_count <= 1:
                        return string_to_compare, other_string
            return compare_strings_in_list(list_of_strings)


filename = os.path.join(os.path.dirname(__file__), 'day2_input.txt')
line_list, matches = file.load_file_list_function(filename, str.rstrip, compare_strings_in_list)
print(f"Real: Found matching strings '{matches[0]}' and '{matches[1]}'.")
answer = ""
for index in range(0, len(matches[0])):
    if matches[0][index] == matches[1][index]:
        answer = answer + matches[0][index]
print(f"The answer is '{answer}'")
