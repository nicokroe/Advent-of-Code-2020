from pathlib import Path
from collections import defaultdict
from typing import Dict
import timeit


def get_input() -> Dict[str, str]:
    input_path = Path(__file__).parent / "bb.txt"
    data = defaultdict()
    for line in input_path.open():
        v, k = line.strip().split(":")
        data[k] = v
    print(len(data))
    return data  # Example: {"kkodfk": "1-3 k"}

def part1(data: Dict) -> int:
    valid = 0
    for k, v in data.items():
        occ, char = v.split()
        lower, upper = occ.split("-")
        if int(lower) <= k.strip().count(char) <= int(upper):
            valid += 1
    return valid

def part2(data: Dict) -> int:
    valid = 0
    for k, v in data.items():
        k = k.strip()
        occ, char = v.split()
        pos1, pos2 = occ.split("-")
        pos1 = int(pos1)-1
        pos2 = int(pos2)-1
        if (k[pos1] is char) ^ (k[pos2] is char):
            valid += 1
    return valid

if __name__ == "__main__":
    data = get_input()
    print(f'Parsing: {timeit.timeit(stmt="data = get_input()", number=5, setup="from __main__ import get_input")*1000/5:.5f} ms')
    print(part1(data))
    print(f'Part 1: {timeit.timeit(stmt="part1(data)", number=5, setup="from __main__ import part1, get_input; data=get_input();")*1000/5:.5f} ms')
    print(part2(data))
    print(f'Part2: {timeit.timeit(stmt="part2(data)", number=5, setup="from __main__ import part2, get_input; data=get_input();")*1000/5:.5f} ms')