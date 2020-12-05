import os
import strutils
import math
import sequtils

proc solve(): void =
    var
        min = high(uint64)
        max: uint64
        sum: uint64
        seat_id: uint64
    var input_path = currentSourcePath().parentDir() & r"\bigboy.txt"
    for line in input_path.readFile().splitLines():
        seat_id = 0
        for i, c in line:
            if c == 'B' or c == 'R':
                seat_id += uint64(2^(len(line)-i-1))
        sum += seat_id
        if seat_id < min: min = seat_id
        if seat_id > max: max = seat_id
    #part 1
    echo max
    #part 2
    var allseats = toSeq(min..max)
    echo math.sum(allseats) - sum

solve()