from pathlib import Path
import timeit

def get_input() -> set[int]:
    input_path = Path(__file__).parent / "input.txt"
    trans_table = {ord("B"): "1", ord("R"): "1", ord("F"): "0", ord("L"): "0"}
    data = set(int(line.translate(trans_table), base=2) for line in input_path.open())
    return data

def solve(data: set[int]) -> tuple[int, int]:
    my_seat = 0
    min_seat = int(min(data))
    max_seat = int(max(data))
    for elem in range(min_seat, max_seat):
        if elem not in data:
            my_seat = elem
    return (max_seat, my_seat)

data = get_input()
print(solve(data))
print(f'Part 1: {timeit.timeit(stmt="solve(data)", number=5, setup="from __main__ import solve, get_input; data=get_input();")*1000/5:.5f} ms')