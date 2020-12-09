from pathlib import Path

def get_input() -> list[int]:
    input_path = Path(__file__).parent / "input.txt"
    data = []
    for line in input_path.open().readlines():
        data.append(int(line.strip()))
    return data

def part1(data: list[int], preamble: int = 5) -> int:
    left_pointer = 0
    right_pointer = preamble
    numbers_to_check = data[preamble:]
    for j in numbers_to_check:
        preamble_set = set(data[left_pointer:right_pointer])
        result_set = set()
        for index in range(left_pointer, right_pointer):
            result_set.add(j-data[index])
        if len(result_set&preamble_set) == 0:
            return j
        left_pointer += 1
        right_pointer += 1
    return -1

def part2(data: list[int], invalid_num: int) -> int:
    for index in range(len(data)):
        sum = 0
        dataslice = data[index:]
        smallest = data[index]
        largest = 0
        for number in dataslice:
            sum += number
            if number > invalid_num:
                break
            elif sum == invalid_num:
                return smallest+largest
            if number < smallest: smallest = number
            if number > largest: largest = number
    return -1


data = get_input()
invalid_num = part1(data, 25)
print(part2(data, invalid_num))