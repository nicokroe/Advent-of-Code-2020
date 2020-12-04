import strutils
import tables
import math
from algorithm import product

proc get_input(): seq[int] =
    let f = readFile("input.txt").splitLines()
    var data: seq[int] = @[]
    for line in f:
        data.add(line.parseInt)
    return data

proc part1(data: seq[int]): int =
    var dict = initTable[int, int]()

    for num in data:
        dict[2020-num] = num

    for num in data:
        if num in dict:
            return num * dict[num]

proc part2(data: seq[int]): int =
    var dict = initTable[int, seq[int]]()

    for tup in product(@[data,data]):
        var key = 2020-tup[0]-tup[1]
        dict[key] = tup

    for num in data:
        if num in dict:
            return num * math.prod(dict[num])

var data = get_input()
echo part1(data)
echo part2(data)







