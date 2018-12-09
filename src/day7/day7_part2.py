
import os
import re
from collections import defaultdict


def find_the_path(filename, total_workers, time_buffer):
    """
    >>> find_the_path("day7_example.txt", 2, 0)
    ('CABFDE', 15)

    :param filename: The name of the file to get the precondition inputs from.
    :return: The correct process order.
    """
    input_file = open(os.path.join(os.path.dirname(__file__), filename), 'r')
    steps = set()
    requirements = defaultdict(set)
    workers = dict()
    working = dict()

    for worker_num in range(0, total_workers):
        workers[worker_num] = 0

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
    total_time = 0
    sorted_steps = sorted(steps)
    while len(sorted_steps) > 0 or any(workers.values()):
        if not all(workers.values()):
            for step in sorted_steps:
                requirements_met = True
                for requirement in requirements[step]:
                    if requirement in sorted_steps or requirement in working.values():
                        requirements_met = False
                        break
                if requirements_met:
                    for worker_id in workers.keys():
                        if workers[worker_id] == 0:
                            working[worker_id] = step
                            workers[worker_id] = 1 + time_buffer + ord(step) - ord("A")
                            sorted_steps.remove(step)
                            break
        if any(workers.values()):
            for worker_id in workers.keys():
                if workers[worker_id] > 0:
                    workers[worker_id] -= 1
                    if workers[worker_id] == 0:
                        answer += working[worker_id]
                        working[worker_id] = ""
        total_time += 1
    return answer, total_time

if __name__ == "__main__":
    process_answer, time = find_the_path('day7_input.txt', 5, 60)
    print(f"The answer is {process_answer} and it took {time}")
