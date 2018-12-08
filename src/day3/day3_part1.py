import re, os
from helper.input_output import file
from collections import defaultdict
'''
    #(\d+)\@(\d+),(\d+):(\d+)x(\d+)
    Capture Group 1: ID
    Capture Group 2: inches from left edge (x)
    Capture Group 3: inches from top (y)
    Capture Group 4: width of claim
    Capture Group 5: height of claim
'''


def process_claims(claim_string, **kwargs):
    """

    :param claim_string: The claim string in format #ID @ x,y: widthxheight
    :param kwargs: The keyword args where we'll get the dictionary for the grid from by name "grid"
    :return: The claim string and the area of the claim


    >>> process_claims("#1 @ 1,3: 4x4", **{"grid":defaultdict(int)})
    ('#1 @ 1,3: 4x4', 16)
    """
    matcher = re.match("#(\d+)\s+@\s+(\d+),(\d+):\s+(\d+)x(\d+)", str.strip(claim_string))
    if matcher is None:
        raise RuntimeError(f"Could not match against the claim string {str.strip(claim_string)}")

    # This grid is not going to be zero-indexed
    x = int(matcher.group(2)) + 1
    y = int(matcher.group(3)) + 1
    width = int(matcher.group(4))
    height = int(matcher.group(5))

    '''
    Don't process this if it's going to exceed the grid's size. 
    We use 1001 because in the loop below the range function creates a range from start (inclusive), to end (exclusive)
    '''
    if x + width > 1001 or y + height > 1001:
        raise ValueError(f"Claim is out of bounds of the rectangle for the grid. Starting point: {x},{y} Height: {height} Width: {width}")

    for current_y in range (y, y+height):
        for current_x in range (x, x+width):
            kwargs["grid"][f"{current_x},{current_y}"] += 1
    return matcher.group(0), width * height  # Return only necessary for testing.


def find_cells_with_overlap(grid_dict):
    overlap = 0
    for cell_key in grid_dict.keys():
        if grid_dict[cell_key] > 1:
            overlap += 1
    return overlap


grid = defaultdict(int)
args = {"grid": grid}
filename = os.path.join(os.path.dirname(__file__), 'day3_input.txt')
file.load_file_iterative_function(filename, process_claims, **args)
overlapping = find_cells_with_overlap(grid)

print(f"Number of overlapping cells is {overlapping}")