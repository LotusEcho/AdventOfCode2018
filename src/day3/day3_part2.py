import re, os
from helper.input_output import file
from collections import defaultdict

class Claim:
    def __init__(self, claim_id, x, y, height, width):
        self.id = claim_id
        self.x = x
        self.y = y
        self.height = height
        self.width = width

def process_claims(claim_string, **kwargs):
    """

    :param claim_string: The claim string in format #ID @ x,y: widthxheight
    :param kwargs: The keyword args where we'll get the dictionary for the grid from by name "grid"
    :return: The claim string and the area of the claim


    >>> claim_obj, area = process_claims("#1 @ 1,3: 4x4", **{"grid":defaultdict(int)})
    >>> print(area)
    16
    >>> print(claim_obj.id)
    1
    >>> print(f"{claim_obj.x},{claim_obj.y}")
    2,4
    """
    matcher = re.match("#(\d+)\s+@\s+(\d+),(\d+):\s+(\d+)x(\d+)", str.strip(claim_string))
    if matcher is None:
        raise RuntimeError(f"Could not match against the claim string {str.strip(claim_string)}")

    # This grid is not going to be zero-indexed
    id = int(matcher.group(1))
    x = int(matcher.group(2)) + 1
    y = int(matcher.group(3)) + 1
    width = int(matcher.group(4))
    height = int(matcher.group(5))

    new_claim = Claim(id, x, y ,height, width)
    '''
    Don't process this if it's going to exceed the grid's size. 
    We use 1001 because in the loop below the range function creates a range from start (inclusive), to end (exclusive)
    '''
    if x + width > 1001 or y + height > 1001:
        raise ValueError(f"Claim is out of bounds of the rectangle for the grid. Starting point: {x},{y} Height: {height} Width: {width}")

    for current_y in range (y, y+height):
        for current_x in range (x, x+width):
            kwargs["grid"][f"{current_x},{current_y}"] += 1
    return new_claim, width * height


def reprocess_claims(claim_list, grid_dict):
    for claim in claim_list:
        isGood = True
        for current_y in range (claim.y, claim.y+claim.height):
            if not isGood:
                break
            for current_x in range (claim.x, claim.x+claim.width):
                if grid_dict[f"{current_x},{current_y}"] > 1:
                    isGood = False
                    break
        if isGood:
            return claim.id
    return None


grid = defaultdict(int)
args = {"grid": grid}
filename = os.path.join(os.path.dirname(__file__), 'day3_input.txt')
the_claims = file.load_file_iterative_function(filename, process_claims, **args)
answer = reprocess_claims(the_claims[0], grid) 
print(f"The good claim is claim#{answer}")
