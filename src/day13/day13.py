import os
from collections import deque
from datetime import datetime


class Cart:
    rep_mapping = {
        '<': [-1, 0],
        '^': [0, -1],
        '>': [1, 0],
        'v': [0, 1]
    }
    left_mapping = {'<': 'v', '^': '<', '>': '^', 'v': '>'}
    straight_mapping = {'<': '<', '^': '^', '>': '>', 'v': 'v'}
    right_mapping = {'<': '^', '^': '>', '>': 'v', 'v': '<'}

    def __init__(self, x, y, representation):
        self.x = x
        self.y = y
        self.direction = representation
        self.last_turn = 0
        self.turn_queue = deque([Cart.left_mapping, Cart.straight_mapping, Cart.right_mapping])

    def move(self, current_round):
        x_mod, y_mod = Cart.rep_mapping[self.direction]
        self.x += x_mod
        self.y += y_mod
        self.last_turn = current_round
        return self.loc_key()

    def turn(self, direction):
        if direction is None:
            self.direction = self.turn_queue[0][self.direction]
            self.turn_queue.rotate(-1)
        else:
            self.direction = direction

    def loc_key(self):
        return f"{self.x},{self.y}"


class Track:
    rep_mapping = {
        "|": {'^': '^', 'v': 'v'},
        "-": {'<': '<', '>': '>'},
        "/": {'<': 'v', '^': '>', '>': '^', 'v': '<'},
        "\\": {'<': '^', '^': '<', '>': 'v', 'v': '>'},
        "+": {'<': None, '^': None, '>': None, 'v': None}
    }
    '''
        This mapping only works if the carts don't start on an intersection or turn.
        My inputs don't, so I'm good.
    '''
    cart_to_track_mapping = {
        '<': '-',
        '^': '|',
        '>': '-',
        'v': '|'
    }

    def __init__(self, x, y, representation):
        self.x = x
        self.y = y
        self.representation = representation
        self.cart = None

    def loc_key(self):
        return f"{self.x},{self.y}"

    def __add__(self, other):
        return int(self) + int(other)

    def __radd__(self, other):
        return int(self) + int(other)

    def __int__(self):
        return int(self.cart is not None)

    def __str__(self):
        if self.cart is None:
            return self.representation
        else:
            return self.cart.direction


def read_track_state(filename):
    """
    >>> test_x, test_y, test_tracks = read_track_state('day13_simple_example.txt')
    >>> test_x
    1
    >>> test_y
    7
    >>> len(test_tracks)
    7
    >>> sum(test_tracks.values())
    2
    >>> test_x, test_y, test_tracks = read_track_state('day13_example.txt')
    >>> test_x
    13
    >>> test_y
    6
    >>> len(test_tracks)
    48
    >>> sum(test_tracks.values())
    2

    :param filename:
    :return:
    """
    input_file = open(os.path.join(os.path.dirname(__file__), filename), 'r')
    grid_x = 0
    grid_y = 0
    track_map = dict()

    for line in input_file:
        current_grid_x = 0
        for character in line.rstrip():
            if character in Track.rep_mapping:
                new_track = Track(current_grid_x, grid_y, character)
                track_map[new_track.loc_key()] = new_track
            elif character in Cart.rep_mapping:
                new_cart = Cart(current_grid_x, grid_y, character)
                new_track = Track(current_grid_x, grid_y, Track.cart_to_track_mapping[character])
                new_track.cart = new_cart
                track_map[new_track.loc_key()] = new_track
            current_grid_x += 1

        grid_y += 1
        grid_x = max(grid_x, current_grid_x)

    return grid_x, grid_y, track_map


def iterate_over_tracks(size_x, size_y, tracks, do_print, stop_over_tracks):
    """
    >>> test_x, test_y, test_tracks = read_track_state('day13_simple_example.txt')
    >>> iterate_over_tracks(test_x, test_y, test_tracks, True, True)
    |
    |
    v
    |
    ^
    |
    |
    Next iteration
    Collision at 0,3
    |
    |
    |
    X
    |
    |
    |
    >>> test_x, test_y, test_tracks = read_track_state('day13_example.txt')
    >>> iterate_over_tracks(test_x, test_y, test_tracks, False, True)
    Collision at 7,3
    >>> test_x, test_y, test_tracks = read_track_state('day13_part2_example.txt')
    >>> iterate_over_tracks(test_x, test_y, test_tracks, False, False)
    Collision at 2,0
    Collision at 2,4
    Collision at 6,4
    Collision at 2,4
    Final cart: 6,4

    :param size_x: The max x of the grid
    :param size_y: The max y of the grid
    :param tracks: The dictionary containing the tracks
    :param do_print: Should we print out the text string?
    :return:
    """
    collision = False

    current_round = 0
    while True:
        current_round += 1
        for y in range(0, size_y):
            if not collision:
                for x in range(0, size_x):
                    current_coords = f"{x},{y}"
                    # If it's here, it's go time!
                    if current_coords in tracks:
                        current_track = tracks[current_coords]
                        # We have a cart, let's get moving!
                        if current_track.cart is not None:
                            current_cart = current_track.cart
                            if current_cart.last_turn < current_round:
                                new_position = current_cart.move(current_round)
                                new_track = tracks[new_position]
                                if new_track.cart is not None:
                                    current_track.cart = None
                                    print(f"Collision at {new_position}")
                                    if stop_over_tracks:
                                        new_track.cart.direction = 'X'
                                        collision = True
                                        break
                                    else:
                                        new_track.cart = None
                                else:
                                    new_track.cart = current_cart
                                    current_track.cart = None
                                    current_cart.turn(Track.rep_mapping[new_track.representation][current_cart.direction])
                    if collision:
                        break
        if do_print:
            for printy in range(0, size_y):
                current_line = ""
                for printx in range(0, size_x):
                    current_coords = f"{printx},{printy}"
                    if current_coords in tracks:
                        current_line += str(tracks[current_coords])
                    else:
                        current_line += " "
                print(current_line)

        if collision:
            break
        elif sum(tracks.values()) <= 1:
            for printy in range(0, size_y):
                for printx in range(0, size_x):
                    current_coords = f"{printx},{printy}"
                    if current_coords in tracks:
                        if tracks[current_coords].cart is not None:
                            print(f"Final cart: {tracks[current_coords].cart.loc_key()}")
            break
        if do_print:
            print("Next iteration")


if __name__ == "__main__":
    start_time = datetime.now()
    real_x, real_y, real_tracks = read_track_state('day13_input.txt')
    print("Part one answer:")
    iterate_over_tracks(real_x, real_y, real_tracks, False, True)

    print("Part two answer:")
    real_x, real_y, real_tracks = read_track_state('day13_input.txt')
    iterate_over_tracks(real_x, real_y, real_tracks, False, False)
