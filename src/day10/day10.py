import os
import re
from datetime import datetime


class Point:

    def __init__(self, x, y, delta_x, delta_y):
        self.x = x
        self.y = y
        self.delta_x = delta_x
        self.delta_y = delta_y

    def move(self, number):
        self.x += (self.delta_x * number)
        self.y += (self.delta_y * number)

        return self

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def distance(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)


def run_until_distance(points):

    seconds = 0

    while True:
        seconds += 1
        points_map = map(lambda point: point.move(1), points)
        current_points = list(points_map)
        max_y = max([point.y for point in current_points])
        min_y = min([point.y for point in current_points])
        distance = abs(min_y - max_y)
        if distance <= 10:  # Chosen experimentally given that the text would need a fixed pixel height.
            break
    return points, seconds


def print_points(points):
    """

    >>> points = process_coordinate_file("day10_example.txt")
    >>> print_points([point.move(3) for point in points])
    #...#..###
    #...#...#.
    #...#...#.
    #####...#.
    #...#...#.
    #...#...#.
    #...#...#.
    #...#..###

    :param points: The list of points to print out.
    :return: Nothing. This just prints a thing.
    """
    minx = min([point.x for point in points])
    miny = min([point.y for point in points])
    maxx = max([point.x for point in points])
    maxy = max([point.y for point in points])

    for y in range(miny, maxy+1):
        line = ""
        for x in range(minx, maxx+1):
            current_point = Point(x, y, 0, 0)
            if current_point in points:
                line += "#"
            else:
                line += "."
        print(line)


def process_coordinate_file(filename):
    """
    >>> points = process_coordinate_file("day10_example.txt")
    >>> len(points)
    31
    >>> points[0].x
    9
    >>> points[0].y
    1
    >>> points[2].y
    -2
    >>> points[2].delta_x
    -1

    :param filename: The name of the file to parse.
    :return: The list of points as they were at time 0
    """
    input_file = open(os.path.join(os.path.dirname(__file__), filename), 'r')
    points = list()

    for line in input_file:
        matcher = re.match("position=<([-|\s]*\d+),\s+(-*\d+)>\svelocity=<([-|\s]*\d+),\s+(-*\d+)>", line)
        if matcher is not None:
            initial_x = int(matcher.group(1).strip())
            initial_y = int(matcher.group(2).strip())
            velocity_x = int(matcher.group(3).strip())
            velocity_y = int(int(matcher.group(4).strip()))
            new_point = Point(initial_x, initial_y, velocity_x, velocity_y)
            points.append(new_point)
        else:
            raise ValueError(f"Could not parse file line= {line.rstrip()}")
    return points


if __name__ == "__main__":
    start_time = datetime.now()
    the_points = process_coordinate_file("day10_input.txt")
    the_points, time = run_until_distance(the_points)
    print_points(list(the_points))
    print(f"Time to calculate answer in world: {time} seconds")
    print(f"Actual runtime of algorithm: {datetime.now() - start_time}")
