from datetime import datetime

"""
This is my attempt at a more efficient algorithm than the one I did in part 1. It doesn't work.
"""


def max_sublist(a_list):
    """ Kadane's Algorithm
    >>> max_sublist([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    (6, 3, 6)
    >>> max_sublist([0, -1, 2,- 3, 5, 9, -5, 10])
    (19, 4, 7)

    :param a_list: The list to get the maximum sub-list for.
    :return: The sum from the sublist, the start index, and the end index. The last two are for testing.
    """
    max_ending_here = max_so_far = a_list[0]
    current_index = 0
    start_index = 0
    end_index = 0
    for num in a_list:
        max_ending_here = max(0, max_ending_here + num)
        if max_ending_here >= max_so_far:
            end_index = current_index
        if max_ending_here == 0:
            start_index = current_index + 1
        max_so_far = max(max_so_far, max_ending_here)
        current_index += 1

    return max_so_far, start_index, end_index


def build_grid(grid_id):
    """

    :param grid_id: Number used to calculate the power values
    :return: The two dimensional list for the 300x300 grid
    """
    grid_values = [[0 for _ in range(300)] for _ in range(300)]
    for x in range(1, 301):
        for y in range(1, 301):
            grid_values[x-1][y-1] = int(str(((x + 10) * y + grid_id) * (x + 10))[-3]) - 5
    return grid_values


def slice_grid(grid_values):
    """
    >>> grid = build_grid(6548)
    >>> slice_grid(grid)
    '233,250 size: 12 max_sum: 121'

    :param grid_values:
    :return:
    """
    max_sum = 0
    left_x = 0
    left_y = 0
    right_x = 0
    right_y = 0

    for left_side in range(0, 300):
        for right_side in range(left_side, 300):
            current_list = list()
            for point in range(0, 300):
                current_list.append(grid_values[point][right_side])
            current_sum, start_y, end_y = max_sublist(current_list)
            if current_sum > max_sum:
                max_sum = current_sum
                if left_x > left_side:
                    left_x = left_side
                if right_x > right_side:
                    right_x = right_side
                if start_y > left_y:
                    left_y = start_y
                if end_y > right_y:
                    right_y = end_y
    return f"{left_x},{left_y} size: {abs(right_y - left_y)} max_sum: {max_sum}"


if __name__ == "__main__":
    start_time = datetime.now()
    grid = build_grid(6548)
    mid_time = datetime.now()
    print(f"Took {mid_time - start_time} to build the grid.")
    answer = slice_grid(grid)
    end_time = datetime.now()
    print(f"Took {end_time - mid_time} more seconds to come up with the answer of {answer} "
          f"for a total runtime of {end_time - start_time}")
