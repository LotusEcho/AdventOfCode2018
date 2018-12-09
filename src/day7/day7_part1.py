import os
import re
from collections import defaultdict


def find_the_path(filename):
    """
    >>> find_the_path("day7_example.txt")
    'CABDFE'
    >>>
    :param filename: The name of the file to get the precondition inputs from.
    :return: The correct process order.
    """
    input_file = open(os.path.join(os.path.dirname(__file__), filename), 'r')
    steps = set()
    requirements = defaultdict(set)

    for line in input_file:
        matcher = re.match("Step\s(\w).*step\s(\w).*", line)
        if matcher is not None:
            precondition = matcher.group(1)
            postcondition = matcher.group(2)

            steps.add(precondition)
            steps.add(postcondition)
            requirements[postcondition].add(precondition)
        else:
            raise ValueError(f"Could not find a match with {line}")
    answer = ""
    sorted_steps = sorted(steps)
    while len(sorted_steps) > 0:
        for step in sorted_steps:
            requirements_met = True
            for requirement in requirements[step]:
                if requirement in sorted_steps:
                    requirements_met = False
                    break
            if requirements_met:
                answer += step
                sorted_steps.remove(step)
                break
    return answer


if __name__ == "__main__":
    print(f"The answer is {find_the_path('day7_input.txt')}")

