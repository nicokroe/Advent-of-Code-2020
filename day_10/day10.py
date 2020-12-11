from pathlib import Path
from functools import lru_cache

def get_input() -> list[int]:
    data = [int(line) for line in (Path(__file__).parent / "input.txt").open().readlines()]
    data.sort()
    return data

data = get_input()
data.insert(0, 0)
data.append(data[-1]+3)

def part1() -> int:
    occurences = {1: 0, 2: 0, 3: 0}
    last_plug = 0
    for plug in data[1:]:
        occurences[plug-last_plug] += 1
        last_plug = plug
    occurences[3] += 1
    return occurences[1]*occurences[3]

@lru_cache(maxsize=100)
def part2(index):
    if index == len(data)-1:
        return 1
    counter = 0
    for j in range(index+1, len(data)):
        if data[j] - data[index] <= 3:
            counter += part2(j) 
        else:
            break
    return counter


 
print(part1())
print(part2(0))
