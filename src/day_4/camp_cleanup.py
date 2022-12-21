from typing import List


def process_input(file_name):
    pairs_list = {}
    with open(file_name) as records:
        for p_id, pair in enumerate(records):
            p1, p2 = pair.strip().split(",")
            p1_v1, p1_v2 = p1.split('-')
            p2_v1, p2_v2 = p2.split('-')
            pairs_list[p_id] = [(int(p1_v1), int(p1_v2)), (int(p2_v1), int(p2_v2))]
        return pairs_list


def contains(l_pair, r_pair) -> bool:
    a, b = l_pair
    x, y = r_pair
    if a >= x and b <= y:
        return True
    if x >= a and y <= b:
        return True
    return False


def overlaps(l_pair, r_pair) -> bool:
    a, b = l_pair
    x, y = r_pair
    if b >= x and a <= y:
        return True
    if b >= y >= a:
        return True
    return False


def overlap_range_count_part_1(pairs_list: dict[int, list[tuple[int, int]]]) -> int:
    count = 0
    for p1, p2 in pairs_list.values():
        count += 1 if contains(p1, p2) else 0
    return count


def overlap_range_count_part_2(pairs_list: dict[int, list[tuple[int, int]]]) -> int:
    count = 0
    for p1, p2 in pairs_list.values():
        count += 1 if overlaps(p1, p2) else 0
    return count


if __name__ == "__main__":
    range_pairs = process_input("./input.in")
    print(f"[Part 1] Overlapping ranges number is: ", overlap_range_count_part_1(range_pairs))
    print(f"[Part 2] Overlapping ranges number is: ", overlap_range_count_part_2(range_pairs))

