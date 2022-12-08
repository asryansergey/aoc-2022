from typing import List
from collections import defaultdict
import re


def process_input(file_name):
    stack_content = []
    commands = []
    with open(file_name) as records:
        row = records.readline()
        while not re.search("[0-9]", row):
            row_data = []
            for idx in range(0, len(row), 4):
                elem = re.search("[A-Z]", row[idx:idx + 2])
                if elem:
                    row_data.append(elem.group(0))
                else:
                    row_data.append('_')
            stack_content.append(row_data)
            row = records.readline()
        records.readline()  # skip the empty line

        for row in records.readlines():
            c, f, t = list(map(lambda x: int(x), re.findall('[0-9]+', row)))  # c == count, f == from, t == to
            commands.append((c, f, t))

    stack_data = defaultdict(list)
    for idx, col in enumerate([*zip(*stack_content)], 1):
        stack_data[idx] = [elem for elem in col[::-1] if elem != '_']

    return stack_data, commands


def stack_top_part_1(stack_data: dict[any], cmds: List[tuple]) -> List[str]:
    for k, v in stack_data.items():
        print(f"{k} => ", *v)
    for c in cmds:
        print(c)
    # write the logic


if __name__ == "__main__":
    stack_entries, commands = process_input("./input.in")
    print(f"[Part 1] Top elements of the stack: ", stack_top_part_1(stack_entries, commands))
