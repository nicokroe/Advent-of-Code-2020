from pathlib import Path
from typing import Set, Tuple, List
import timeit

def get_input() -> list[str]:
    input_path = Path(__file__).parent / "input.txt"
    data = []
    for line in input_path.open():
        data.append(line.strip())
    return data
def compute_seat(seat: str, low: int, high: int) -> int:
    low = low
    high = high
    for char in seat:
        if char == "F" or char == "L":
            high = int((high-low)/2)+low
        else:
            low = int((high-low)/2)+low+1
    return low

def solve(data: list[str]) -> Tuple[int, int]:
    ids: Set[int] = set()
    my_seat = 0
    for seat in data:
        row = compute_seat(seat[:7], 0 ,127)
        column = compute_seat(seat[-3:], 0 ,7)
        ids.add(row*8+column)
    min_seat = min(ids)
    max_seat = max(ids)
    for elem in range(min_seat, max_seat+1):
        if elem not in ids:
            my_seat = elem
    return (int(max_seat), my_seat)

data = get_input()
print(solve(data))
print(f'Part 1: {timeit.timeit(stmt="solve(data)", number=5, setup="from __main__ import solve, get_input; data=get_input();")*1000/5:.5f} ms')