import os
import re
from collections import defaultdict

input_file = open(os.path.join(os.path.dirname(__file__), 'day6_input.txt'), 'r')
min_x = -1
min_y = -1
max_x = -1
max_y = -1
points = []

for line in input_file:
    matcher = re.match("(\d+),\s(\d+)", line)
    if matcher is not None:
        y = int(matcher.group(1))
        x = int(matcher.group(2))
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y
        if min_x == -1 or min_y == -1:
            min_x = x
            min_y = y
        else:
            if x < min_x:
                min_x = x
            if y < min_y:
                min_y = y
        point_string = f"{y},{x}"
        points.append(point_string)


def calculate_distances(minx, maxx, miny, maxy):
    distances = defaultdict(lambda:1)
    for x_point in range(minx, maxx+1):
        for y_point in range(miny, maxy+1):
            point_string = f"{y_point},{x_point}"
            if point_string not in points:
                min_point_value = 100
                min_point = None
                for point in points:
                    matcher = re.match("(\d+),(\d+)", point)
                    if matcher is not None:
                        y = int(matcher.group(1))
                        x = int(matcher.group(2))
                        current_point_value = abs(x - x_point) + abs(y - y_point)
                        if current_point_value < min_point_value:
                            min_point_value = current_point_value
                            min_point = point
                    else:
                        raise ValueError(f"Formatting was wrong for {point}")
                for point in points:
                    matcher = re.match("(\d+),(\d+)", point)
                    if matcher is not None:
                        y = int(matcher.group(1))
                        x = int(matcher.group(2))
                        current_point_value = abs(x_point - x) + abs(y_point -y)
                        if point != min_point and current_point_value == min_point_value:
                            min_point = None
                    else:
                        raise ValueError(f"Formatting was wrong for {point}")
                if min_point is not None:
                    distances[min_point] += 1
    return distances


print(f"Grid dimensions: {min_x}, {min_y} to {max_x}, {max_y}")
max_point_area = 0
max_point = None
orig_distances = calculate_distances(min_x, max_x, min_y, max_y)
bigger_distances = calculate_distances(min_x -1, max_x +1, min_y -1, max_y+1)
distances = dict()
for distance_key in orig_distances:
    if orig_distances[distance_key] == bigger_distances[distance_key]:
        distances[distance_key] = orig_distances[distance_key]

for point in distances.keys():
    if distances[point] > max_point_area:
        max_point = point
        max_point_area = distances[point]
    print(f"{point} = {distances[point]}")
print(f"Max point is {max_point} with distance {max_point_area}")
