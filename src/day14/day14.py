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

    :param improvement_num:
    :param count:
    :return:
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


if __name__ == "__main__":
    start_time = datetime.now()
    part1 = find_good_recipes(793061, 10)
    print(f"Answer to part 1 was {part1} after {datetime.now() - start_time}")
    mid_time = datetime.now()
    