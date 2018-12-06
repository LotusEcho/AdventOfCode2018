import os
import re

input_file = open(os.path.join(os.path.dirname(__file__), 'day6_input.txt'), 'r')
minx = -1
miny = -1
maxx = -1
maxy = -1
points = []
max_distance = 10000

for line in input_file:
    matcher = re.match("(\d+),\s(\d+)", line)
    if matcher is not None:
        y = int(matcher.group(1))
        x = int(matcher.group(2))
        if x > maxx:
            maxx = x
        if y > maxy:
            maxy = y
        if minx == -1 or miny == -1:
            minx = x
            miny = y
        else:
            if x < minx:
                minx = x
            if y < miny:
                miny = y
        point_string = f"{y},{x}"
        points.append(point_string)

total_safe_area = 0
for x_point in range(minx, maxx+1):
    for y_point in range(miny, maxy+1):
        point_string = f"{y_point},{x_point}"
        total_point_value = 0
        for point in points:
            matcher = re.match("(\d+),(\d+)", point)
            if matcher is not None:
                y = int(matcher.group(1))
                x = int(matcher.group(2))
                current_point_value = abs(x - x_point) + abs(y - y_point)
                total_point_value += current_point_value
                if total_point_value >= max_distance:
                    break
            else:
                raise ValueError(f"Formatting was wrong for {point}")
        if total_point_value < max_distance:
            total_safe_area += 1
print(f"Total safe area is {total_safe_area}")
