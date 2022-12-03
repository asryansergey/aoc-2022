from typing import List


def process_input(file_name):
    with open(file_name) as records:
        return [pair.strip().split(' ') for pair in records]


def round_score_part_1(shape_1, shape_2):
    shape_value = {'X': 1, 'Y': 2, 'Z': 3}
    win_round_score, draw_round_score, lose_round_score = 6, 3, 0

    if ord(shape_2) - ord(shape_1) == 23:
        return draw_round_score + shape_value[shape_2]

    if shape_1 == 'A' and shape_2 == 'Y':
        return win_round_score + shape_value[shape_2]
    elif shape_1 == 'B' and shape_2 == 'Z':
        return win_round_score + shape_value[shape_2]
    elif shape_1 == 'C' and shape_2 == 'X':
        return win_round_score + shape_value[shape_2]
    else:
        return shape_value[shape_2]

def round_score_part_2(shape_1, shape_2):
    win_pairs = {'A': 'Y', 'B': 'Z', 'C': 'X'}
    draw_pairs = {'A': 'X', 'B': 'Y', 'C': 'Z'}
    lose_pairs = {'A': 'Z', 'B': 'X', 'C': 'Y'}
    shape_value = {'X': 1, 'Y': 2, 'Z': 3}
    win_round_score, draw_round_score, lose_round_score = 6, 3, 0

    if shape_2 == 'Z':
        return win_round_score + shape_value[win_pairs[shape_1]]
    elif shape_2 == 'Y':
        return draw_round_score + shape_value[draw_pairs[shape_1]]
    else:
        return shape_value[lose_pairs[shape_1]]


def calculate_score(round_pairs: List[List[str]], func):
    total_score = 0
    for pair in round_pairs:
        total_score += func(pair[0], pair[1])
    return total_score


if __name__ == "__main__":
    rps_pairs = process_input("./input.in")
    print(f"[Part 1] Total score is {calculate_score(rps_pairs, round_score_part_1)}")
    print(f"[Part 2] Total score is {calculate_score(rps_pairs, round_score_part_2)}")
