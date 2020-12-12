from pathlib import Path
from typing import Iterator
from time import sleep

def get_input() -> list[bytearray]:
    input_path = Path(__file__).parent / "input.txt"
    data = [bytearray(line, "ascii").strip().replace(b"L", b"#") for line in input_path.open().readlines()]
    return data

def generate_indices(x: int, y: int) -> Iterator[tuple[int, int]]:
    indices = [(x-1, y-1), (x-1, y), (x-1, y+1), (x, y-1), (x, y+1), (x+1, y-1), (x+1, y), (x+1, y+1)]
    for index in indices:
        yield index

def part1(data: list[bytearray]) -> int:
    while True:
        seats_to_change = set()
        for x, seats in enumerate(data):
            for y, seat in enumerate(seats):
                if seat == 46:
                    continue
                else:
                    indices = generate_indices(x, y)
                    occupied_seats = 0
                    for x1, y1 in indices:
                        if 0 <= x1 < len(data) and 0 <= y1 < len(seats):
                            if data[x1][y1] == 35:
                                occupied_seats += 1
                    if occupied_seats >= 4:
                        if seat == 35:
                            seats_to_change.add((x, y))
                    elif not occupied_seats:
                        if seat == 76:
                            seats_to_change.add((x, y))
        if not seats_to_change:
            break
        for x, y in seats_to_change:
            if data[x][y] == 35:
                data[x][y] = 76
            else:
                data[x][y] = 35
    return sum([line.count(35) for line in data])

def part2(data: list[bytearray]) -> int:
    while True:
        seats_to_change = set()
        for x, seats in enumerate(data):
            for y, seat in enumerate(seats):
                if seat == 46:
                    continue
                else:
                    indices = generate_indices(x, y)
                    occupied_seats = 0
                    for x1, y1 in indices:
                        if 0 <= x1 < len(data) and 0 <= y1 < len(seats):
                            if data[x1][y1] == 35:
                                occupied_seats += 1
                    if occupied_seats >= 5:
                        if seat == 35:
                            seats_to_change.add((x, y))
                    elif not occupied_seats:
                        if seat == 76:
                            seats_to_change.add((x, y))
        if not seats_to_change:
            break
        for x, y in seats_to_change:
            if data[x][y] == 35:
                data[x][y] = 76
            else:
                data[x][y] = 35
    return sum([line.count(35) for line in data])     
                

data = get_input()

print(part1(data))