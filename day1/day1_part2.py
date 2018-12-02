#!/usr/bin/python3
import os


def load_file(current_frequency, frequency_set):
    """Takes the starting frequency and reads in the input from our file.

    :param current_frequency: The current frequency the device is at.
    :param frequency_set: The set of frequencies we found after applying the frequency change.
    :return: The current frequency and the list of changes in frequency that we read in from file.
    """
    change_list = list()
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'day1_input.txt')
    file = open(filename, 'r')
    for line in file:
        change = int(line)
        change_list.append(change)
        current_frequency += change
        frequency_set.add(current_frequency)
    file.close()
    return current_frequency, change_list


def brute_force(current_frequency, inputs, frequency_set, current_invocations):
    """Takes in the starting frequency, inputs, and the current frequency set
    and applies the list until it finds a collision.

    :param current_frequency: The current frequency the device is at.
    :param inputs: The list of changes in frequency to apply to the current frequency.
    :param frequency_set: The set of frequencies the device has already been at.
    :param current_invocations: The number of iterations we've done, used to measure efficiency.
    :return: The frequency that appeared twice after applying the inputs and the invocation count.
    """
    for change in inputs:
        current_invocations += 1
        current_frequency += change
        if current_frequency in frequency_set:
            return current_frequency, current_invocations
        frequency_set.add(current_frequency)
    return brute_force(current_frequency, inputs, frequency_set, current_invocations)


first_pass_frequencies = {0}  # Set of frequencies we've found, starting the first one
frequency, input_list = load_file(0, first_pass_frequencies)
assert (frequency == 472)  # Frequency should be 472 with my inputs at this point
brute_force_set = first_pass_frequencies.copy()

brute_force_answer, brute_force_invocations = brute_force(frequency, input_list, brute_force_set, 0)
print(f'Brute Force Method: Found the first repeated frequency {brute_force_answer} in {brute_force_invocations} '
      f'invocations with input size {len(input_list)}')
