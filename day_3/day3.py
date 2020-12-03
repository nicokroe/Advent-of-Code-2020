from pathlib import Path
from math import prod
import timeit

def get_input():
    input_path = Path(__file__).parent / "input.txt"
    data = [line.strip() for line in input_path.open()]
    return data

def part1(data):
    trees = 0
    index = 0
    for line in data:
        if line[index] == "#":
            trees += 1
        index = (index + 3) % len(line) 
    return trees

def part2(data):
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    slope_trees = []
    for slope in slopes:
        trees = 0
        index = 0
        for line in data[::slope[1]]:
            if line[index] == "#":
                trees += 1
            index = (index + slope[0]) % len(line)
        slope_trees.append(trees)        
    return prod(slope_trees)

if __name__ == "__main__":
    data = get_input()
    print(f'Parsing: {timeit.timeit(stmt="data = get_input()", number=5, setup="from __main__ import get_input")*1000/5:.5f} ms')
    print(part1(data))
    print(f'Part 1: {timeit.timeit(stmt="part1(data)", number=5, setup="from __main__ import part1, get_input; data=get_input();")*1000/5:.5f} ms')
    print(part2(data))
    print(f'Part2: {timeit.timeit(stmt="part2(data)", number=5, setup="from __main__ import part2, get_input; data=get_input();")*1000/5:.5f} ms')