from typing import List


def process_input(file_name):
    with open(file_name) as records:
        return [pair.strip() for pair in records]


def get_matching_items(item_pack_1: str, item_pack_2: str) -> List[str]:
    known_items = {i: 1 for i in item_pack_1}
    matching_items = []
    for i2 in item_pack_2:
        if i2 in known_items.keys():
            matching_items.append(i2)
    return matching_items


def return_item_value(item: str) -> int:
    if not item:
        return 0
    return 1 + (ord(item) - ord('a')) if 'a' <= item <= 'z' else 27 + (ord(item) - ord('A'))


def priority_sum_part_1(rucksack_items: List[str]) -> int:
    result = 0
    for item_list in rucksack_items:
        mid_item_idx = len(item_list) // 2
        pack_1, pack_2 = item_list[:mid_item_idx], item_list[mid_item_idx:]
        result += return_item_value(get_matching_items(pack_1, pack_2)[0])
    return result


def priority_sum_part_2(rucksack_items: List[str]) -> int:
    def get_matching_items_in_trio(trio_seq: List[str]) -> str:
        matching_items = get_matching_items(trio_seq[0], trio_seq[1])
        return get_matching_items("".join(matching_items), trio_seq[2])[0]

    result = 0
    for idx in range(0, len(rucksack_items), 3):
        result += return_item_value(get_matching_items_in_trio(rucksack_items[idx:idx + 3]))
    return result


if __name__ == "__main__":
    seq = process_input("./input.in")
    print(f"[Part 1] Priority sum is: ", priority_sum_part_1(seq))
    print(f"[Part 1] Priority sum is: ", priority_sum_part_2(seq))

