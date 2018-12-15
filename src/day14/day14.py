from datetime import datetime


def find_good_recipes(improvement_num, count):
    """
    >>> find_good_recipes(9, 10)
    '5158916779'
    >>> find_good_recipes(5, 10)
    '0124515891'
    >>> find_good_recipes(18, 10)
    '9251071085'
    >>> find_good_recipes(2018, 10)
    '5941429882'

    :param improvement_num: The number of recipes
    :param count: The number of recipes after to look
    :return: The recipes after the given count
    """
    recipes = [3, 7]

    elf1 = 0
    elf2 = 1

    while len(recipes) <= improvement_num + count:
        elf1_value = recipes[elf1]
        elf2_value = recipes[elf2]

        recipe_sum = elf1_value + elf2_value

        if recipe_sum > 9:
            recipe_string = f"{recipe_sum:02d}"
            recipes.append(int(recipe_string[:1]))
            recipes.append(int(recipe_string[1:]))
        else:
            recipes.append(recipe_sum)

        elf1 = loop_around(1 + elf1 + elf1_value, len(recipes))
        elf2 = loop_around(1 + elf2 + elf2_value, len(recipes))

    answer_string = ""
    for i in range(improvement_num, improvement_num + count):
        answer_string += str(recipes[i])
    return answer_string


def loop_around(index, list_length):
    while index >= list_length:
        index -= list_length
    return index


def measure_the_work(pattern_to_find):
    """
    >>> measure_the_work('51589')
    9
    >>> measure_the_work('01245')
    5
    >>> measure_the_work('92510')
    18
    >>> measure_the_work('59414')
    2018

    :param pattern_to_find: The pattern to look for.
    :return: The number of recipes before the holy pattern
    """
    recipes = [3, 7]
    keys = [int(key) for key in pattern_to_find]
    elf1 = 0
    elf2 = 1
    not_found = True

    while not_found:
        elf1_value = recipes[elf1]
        elf2_value = recipes[elf2]

        recipe_sum = elf1_value + elf2_value

        if recipe_sum > 9:
            recipe_string = f"{recipe_sum:02d}"
            recipes.append(int(recipe_string[:1]))
            recipes.append(int(recipe_string[1:]))
        else:
            recipes.append(recipe_sum)

        elf1 = loop_around(1 + elf1 + elf1_value, len(recipes))
        elf2 = loop_around(1 + elf2 + elf2_value, len(recipes))
        if recipes[-1] == keys[-1] or recipes[-2] == keys[-1]:

            if pattern_to_find in ''.join(map(str, recipes[-(len(keys) + 2):])):
                not_found = False
    if recipes[-1] == keys[-1]:
        return len(recipes) - len(keys)
    else:
        return len(recipes) - len(keys) - 1


if __name__ == "__main__":
    start_time = datetime.now()
    part1 = find_good_recipes(793061, 10)
    print(f"Answer to part 1 was {part1} after {datetime.now() - start_time}")
    mid_time = datetime.now()
    part2 = measure_the_work('793061')
    print(f"Answer to part 2 was {part2} after {datetime.now() - mid_time}")
