class StartingPoint:
    def __init__(self, x, y, size, grid):
        self.x = x + 1
        self.y = y + 1
        self.power = 0
        self.size = size
        for x_cord in range(x, x + size):
            for y_cord in range(y, y + size):
                self.power += grid[x_cord][y_cord]

    def __gt__(self, other):
        return self.power > other.power


def build_grid(grid_id, size):
    """
    >>> point = build_grid(18, 3)
    >>> point.x
    33
    >>> point.y
    45
    >>> real_point = build_grid(6548, 3)
    >>> f"{real_point.x},{real_point.y}"
    '21,53'

    :param grid_id: The ID used to generate your grid.
    :param size: The size of the sub-grids to construct
    :return:
    """
    grid_values = [[0 for _ in range(300)] for _ in range(300)]
    starting_points = list()
    for x in range(0, 300):
        for y in range(0, 300):

            grid_values[x][y] = int(str(((x + 11) * (y + 1) + grid_id) * (x + 11))[-3]) - 5
    for x in range(0, 300 - size):
        for y in range(0, 300 - size):
            starting_points.append(StartingPoint(x, y, size, grid_values))

    return max(starting_points)


if __name__ == "__main__":
    starting_points = list()
    for size in range(1, 301):
        current_point = build_grid(6548, size)
        starting_points.append(current_point)
        if current_point.power < 0:
            # Abort, I doubt larger ones will be worth the trouble
            break
    winning_point = max(starting_points)
    print(f"The winning point is {winning_point.x},{winning_point.y} with power {winning_point.power} "
          f"and size {winning_point.size}")
