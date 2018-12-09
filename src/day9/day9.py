from collections import defaultdict, deque
from datetime import datetime

def find_high_score(player_num, last_marble_value):
    """
    >>> find_high_score(7, 25)
    32
    >>> find_high_score(10, 1618)
    8317
    >>> find_high_score(13, 7999)
    146373
    >>> find_high_score(17, 1104)
    2764
    >>> find_high_score(21, 6111)
    54718
    >>> find_high_score(30, 5807)
    37305
    >>> find_high_score(470, 72170)
    388024

    :param player_num: The number of players in this game.
    :param last_marble_value: The value of the last marble played before the game ended.
    :return: The high score for that game.
    """

    player_scores = defaultdict(int)
    marble_locations = deque()
    marble_locations.append(0)
    current_marble_value = 1
    current_index = 0
    while current_marble_value <= last_marble_value:
        for player_id in range(1, player_num + 1):
            if current_marble_value % 23 == 0:
                player_scores[player_id] += current_marble_value
                current_index -= 7
                if current_index < 0:
                    current_index = marble_locations.index(marble_locations[current_index])
                marble_to_remove = marble_locations[current_index]
                player_scores[player_id] += marble_to_remove
                marble_locations.remove(marble_to_remove)
            elif current_marble_value == 1 or len(marble_locations) == current_index + 2:
                marble_locations.append(current_marble_value)
                current_index = len(marble_locations)
            elif current_index + 2 <= len(marble_locations):
                current_index += 2
                current_len = len(marble_locations)
                marble_locations.insert(current_index, current_marble_value)
                assert current_len+1 == len(marble_locations)
            else:
                current_index = 1
                current_len = len(marble_locations)
                marble_locations.insert(1, current_marble_value)
                assert current_len+1 == len(marble_locations)
            current_marble_value += 1
            if current_marble_value > last_marble_value:
                break

    high_score = 0
    winning_player = -1
    for player in player_scores.keys():
        if player_scores[player] > high_score:
            high_score = player_scores[player]
            winning_player = player
    return high_score


if __name__ == "__main__":
    start_time = datetime.now()
    print(f"Part 1 high score: {find_high_score(470, 72170)} Runtime {datetime.now() - start_time}")
    start_time = datetime.now()
    print(f"Part 2 high score: {find_high_score(470, 7217000)} Runtime {datetime.now() - start_time}")
