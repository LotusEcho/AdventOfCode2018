from collections import deque
from datetime import datetime

"""
I converted my original input into binary by replacing "#" with 1 and "," to 0. 
It made comparing easier by leveraging the built-in int function with base 2.
It also made finding the number of plants easy.

"""


def no_game_no_life(seed, rules, iterations, print_list):
    """
    >>> rules = {3 : 1, 4 : 1, 8 : 1, 10 : 1, 11 : 1, 12 : 1, 15 : 1, 21 : 1,
    ... 23 : 1, 26 : 1, 27 : 1, 28 : 1, 29 : 1, 30 : 1}
    >>> current_plants = no_game_no_life('1001010011000000111000111', rules, 20, True)
    1000100001000001001001001
    11001100011000010010010011
    101000100101000010010010001
    101001000101000100100110011
    10001100010100100100010001
    110101000010001001100110011
    1001110100011001000100010001
    10000110101010011001100110011
    11001001111100001000100010001
    1010010001011000011001100110011
    100011000101000101000100010001
    1101010000101000101001100110011
    10011101000010100010000100010001
    100001101000010100110001100110011
    110010010100001000010010100010001
    10100100010100011000100010100110011
    1000110001010101000110001000010001
    11010100001111101010100011000110011
    100111010010101111111010101001010001
    1000011000011111000111111100001010011
    >>> current_plants
    325

    :param seed: The starting binary string.
    :param rules: A dictionary of decimal numbers to 1's and 0's that represent the rules of the game.
    :param iterations: The number of iterations to run.
    :param print_list: Whether or not to print the resulting list
    :return: The number of plants in the last iteration
    """
    pot_queue = deque(list(map(int, list(seed))))
    starting_index = 0

    for iteration in range(0, iterations):
        iteration_queue = deque()
        for _ in range(0, 4):
            pot_queue.append(0)
            pot_queue.appendleft(0)
        current_pot = "0000"
        starting_index -= 6
        while len(pot_queue) > 0:
            current_pot += str(pot_queue.popleft())
            if int(current_pot, 2) in rules:
                iteration_queue.append(rules[int(current_pot, 2)])
            else:
                iteration_queue.append(0)
            current_pot = current_pot[1:]
        pot_queue = iteration_queue
        while True:
            if pot_queue[0] == 0:
                pot_queue.popleft()
                starting_index += 1
            elif pot_queue[-1] == 0:
                pot_queue.pop()
            else:
                break
        if print_list:
            print(''.join(map(str,pot_queue)))

    running_sum = 0
    current_index = starting_index
    for pot in pot_queue:
        if pot == 1:
            running_sum += current_index
        current_index += 1

    return running_sum


if __name__ == "__main__":
    start_time = datetime.now()
    life_rules = {int('00000', 2): 0, int('10011', 2): 0, int('00111', 2): 1, int('00101', 2): 1,
                  int('01010', 2): 0, int('11110', 2): 0, int('11011', 2): 1, int('10000', 2): 0,
                  int('10001', 2): 0, int('00011', 2): 0, int('11001', 2): 0, int('01110', 2): 1,
                  int('11111', 2): 1, int('10100', 2): 1, int('01100', 2): 1, int('01011', 2): 0,
                  int('00010', 2): 1, int('10110', 2): 1, int('00100', 2): 1, int('11000', 2): 1,
                  int('00001', 2): 0, int('11101', 2): 1, int('10010', 2): 1, int('10111', 2): 1,
                  int('11010', 2): 0, int('11100', 2): 1, int('01111', 2): 0, int('01000', 2): 1,
                  int('00110', 2): 0, int('01101', 2): 0, int('10101', 2): 1, int('01001', 2): 0}
    my_seed = "1110000000110000101010011101100110000010000101000001101110001110100011101110101110001011110110100001"
    answer = no_game_no_life(my_seed, life_rules, 20, False)
    print(f"Part 1 answer was {answer} and took {datetime.now() - start_time}")
    start_time = datetime.now()
    answer = no_game_no_life(my_seed, life_rules, 50000000000, False)
    print(f"Part 2 answer was {answer} and took {datetime.now() - start_time}")

