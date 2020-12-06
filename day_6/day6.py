from pathlib import Path
from collections import Counter

def get_input() -> list[str]:
    input_path = Path(__file__).parent / "input.txt"
    data = []
    with input_path.open() as f:
        data = f.read().split("\n\n")
    return data

def part1(data: list[str]) -> int:
    sum = 0
    for group_raw in data:
        group = group_raw.replace("\n", "")
        sum += len(set(group))
    return sum

def part2(data: list[str]) -> int:
    sum = 0
    for group in data:
        counter = Counter()
        persons = group.split()
        for person in persons:
            counter.update(person)
        for num in counter.values():
            if num == len(persons):
                sum += 1 
    return sum

data = get_input()
print(part1(data))
print(part2(data))
