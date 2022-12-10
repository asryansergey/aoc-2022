import copy
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
    # [*zip(*stack_content)] works when lengths of each row in stack_content are equal
    for idx, col in enumerate([*zip(*stack_content)], 1):
        stack_data[idx] = [elem for elem in col[::-1] if elem != '_']

    return stack_data, commands


def elements_to_move_part_1(buffer: List[int]) -> List[int]:
    return buffer[::-1]


def elements_to_move_part_2(buffer: List[int]) -> List[int]:
    return buffer


def stack_top_parts(stack_data: dict[any], cmds: List[tuple], compute_buffer) -> str:
    for c, f, t, in cmds:
        entry_size = len(stack_data[f])
        if entry_size >= c:
            stack_data[t].extend(compute_buffer(stack_data[f][(entry_size-c):]))
            del stack_data[f][entry_size-c:]
    top_elements = "".join([str(row[-1]) for row in stack_data.values() if row])
    return top_elements


if __name__ == "__main__":
    stack_entries, cmd_list = process_input("./input.in")
    print(f"[Part 1] Top elements of the stack: ", stack_top_parts(copy.deepcopy(stack_entries), cmd_list,
                                                                   elements_to_move_part_1))
    print(f"[Part 2] Top elements of the stack: ", stack_top_parts(stack_entries, cmd_list, elements_to_move_part_2))
