from pathlib import Path
from itertools import combinations
from math import prod
import timeit
from collections import defaultdict

def get_input():
    input_path = Path(__file__).parent / "input.txt"
    data = set(int(line) for line in input_path.open())
    return data

def part1(data: set) -> int:
    for tuple in combinations(data, 2):
        if sum(tuple) == 2020:
            return prod(tuple)

def part2(data: set) -> int:
    values = defaultdict()
    for tuple in combinations(data, 2):
        values[sum(tuple)] = prod(tuple)
    for number in data:
        try:
            return values[2020-number]*number
        except KeyError:
            pass


if __name__ == "__main__":
    data = get_input()
    print(part1(data))
    print(timeit.timeit(stmt="part1(data)", number=5, setup="from __main__ import part1, get_input; data=get_input();")/5)
    print(part2(data))
    print(timeit.timeit(stmt="part2(data)", number=5, setup="from __main__ import part2, get_input; data=get_input();")/5)
