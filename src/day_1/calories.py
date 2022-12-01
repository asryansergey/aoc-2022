from typing import List


def process_input(file_name):
    with open(file_name) as records:
        return [calorie.strip() for calorie in records]


def count_calories_per_elf(calorie_values: List[int]) -> List[int]:
    accumulated_calories = []
    per_elf_sum = 0
    for val in calorie_values:
        if val == '':
            accumulated_calories.append(per_elf_sum)
            per_elf_sum = 0
        else:
            per_elf_sum += int(val)
    return accumulated_calories


if __name__ == "__main__":
    calories_list = process_input("./input.in")
    print(f"Max calories: {max(count_calories_per_elf(calories_list))}")
    print(f"Sum of calories for max 3: {sum(sorted(count_calories_per_elf(calories_list))[-3:])}")
