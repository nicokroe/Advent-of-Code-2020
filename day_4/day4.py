from pathlib import Path
import re
import timeit

needed_keys = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}

def get_input() -> list[dict[str, str]]:
    input_path = Path(__file__).parent / "input.txt"
    result = []
    with input_path.open() as f:
        data = f.read().split("\n\n")
    for line in data:
        passport = {}
        for elem in line.split():
            k, v = elem.split(":")
            passport[k] = v
        result.append(passport)
    return result

def check_passport(passport: dict[str, str]) -> bool:
    for k, v in passport.items():
        if k == "byr":
            if not 1920 <= int(v) <= 2002:
                return False
        elif k == "iyr":
            if not 2010 <= int(v) <= 2020:
                return False
        elif k == "eyr":
            if not 2020 <= int(v) <= 2030:
                return False
        elif k == "hgt":
            match = re.match(r"^(\d+)(cm|in)", v, re.I)            
            if not match:
                return False
            height, unit = match.groups()
            if unit == "cm":
                if not 150 <= int(height) <= 193:
                    return False
            elif unit == "in":
                if not 59 <= int(height) <= 76:
                    return False
        elif k == "hcl":
            match = re.match(r"^#([0-9a-f]{6})$", v)
            if not match:
                return False
        elif k == "ecl":
            if not v in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}:
                return False
        elif k == "pid":
            if not len(v) == 9:
                return False
    return True
    

def part1(data: list[dict[str, str]]) -> int:
    valid = 0
    for passport in data:
        if len(passport) == 8:
            valid += 1
        elif len(passport) == 7:
            if not "cid" in passport:
                valid += 1
    return valid

def part2(data: list[dict[str, str]]) -> int:
    valid = 0
    for passport in data:
        if all(k in passport for k in needed_keys):
            if check_passport(passport):
                valid += 1
    return valid

if __name__ == "__main__":
    data = get_input()
    print(f'Parsing: {timeit.timeit(stmt="data = get_input()", number=5, setup="from __main__ import get_input")*1000/5:.5f} ms')
    print(part1(data))
    print(f'Part 1: {timeit.timeit(stmt="part1(data)", number=5, setup="from __main__ import part1, get_input; data=get_input();")*1000/5:.5f} ms')
    print(part2(data))
    print(f'Part2: {timeit.timeit(stmt="part2(data)", number=5, setup="from __main__ import part2, get_input; data=get_input();")*1000/5:.5f} ms')