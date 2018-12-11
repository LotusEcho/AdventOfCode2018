class StartingPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.list_of_points = [f"{nux},{nuy}" for nux in range(x, x + 3) for nuy in range(y, y + 3)]
        self.power = 0

    def __gt__(self, other):
        return self.power > other.power

values = dict()


def build_grid(grid_id):
    """
    >>> point = build_grid(18)
    >>> point.x
    33
    >>> point.y
    45
    >>> real_point = build_grid(6548)
    >>> f"{real_point.x},{real_point.y}"
    '21,53'

    :param grid_id:
    :return:
    """
    starting_points = list()
    for x in range(1, 301):
        for y in range(1, 301):
            values[f'{x},{y}'] = int(str(((x + 10) * y + grid_id) * (x + 10))[-3]) - 5
            if x <= 297 and y <= 297:
                starting_points.append(StartingPoint(x, y))
    return max(map(calculate_power, starting_points))


def calculate_power(starting_point):
    starting_point.power = sum(list(map(lambda point: values[point], starting_point.list_of_points)))
    return starting_point
