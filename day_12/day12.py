from pathlib import Path
from typing import NamedTuple

class Instruction(NamedTuple):
    direction: str
    amount: int

class Waypoint(object):

    def __init__(self, east, south, west, north):
        self.east = east
        self.south = south
        self.west = west
        self.north = north

    def rotate(self, direction: str, amount: int):
        if direction == "L":
            while amount:
                self.east, self.south, self.west, self.north = self.south, self.west, self.north, self.east
                amount -= 90
        else:
            while amount:
                self.east, self.south, self.west, self.north = self.north, self.east, self.south, self.west
                amount -= 90
    
    def update(self, direction: str, amount: int):
        if direction == "E":
            self.east += amount
        elif direction == "S":
            self.south += amount
        elif direction == "W":
            self.west += amount
        elif direction == "N":
            self.north += amount

    def __str__(self) -> str:
        return f"East: {self.east} South: {self.south} West: {self.west} North: {self.north}"

class Ship(object):

    def __init__(self, east: int, south: int, west: int, north: int, direction: int):
        self.east = east
        self.south = south
        self.west = west
        self.north = north
        self.direction = direction

    def move(self, direction: str, amount: int) -> None:
        if direction == "E":
            self.east += amount
        elif direction == "S":
            self.south += amount
        elif direction == "W":
            self.west += amount
        elif direction == "N":
            self.north += amount
    
    def move_to_waypoint(self, waypoint: Waypoint):
        self.east += waypoint.east
        self.south += waypoint.south
        self.west += waypoint.west
        self.north += waypoint.north
    
    def manhattan(self) -> int:
        return abs(self.north-self.south)+abs(self.east-self.west)
    
    def change_direction(self, direction: str, amount: int):
        if direction == "R":
            self.direction = (self.direction + amount) % 360
        elif direction == "L":
            self.direction = (self.direction - amount) % 360

    def __str__(self) -> str:
        return f"East: {self.east} South: {self.south} West: {self.west} North: {self.north}"

def get_input() -> list[Instruction]:
    input_path = Path(__file__).parent / "input.txt"
    data = [Instruction(chr(line[0]), int(line[1:].strip())) for line in input_path.open(mode="rb").readlines()]
    return data

def part1(instructions: list[Instruction]) -> int:
    ship = Ship(0, 0, 0, 0, 0)
    directions = {0: "E", 90: "S", 180: "W", 270: "N"}
    for instruction in instructions:
        if instruction.direction == "R" or instruction.direction == "L":
            ship.change_direction(instruction.direction, instruction.amount)
        elif instruction.direction == "F":
            direction = directions[ship.direction]
            ship.move(direction, instruction.amount)
        else:
            ship.move(instruction.direction, instruction.amount)
    return ship.manhattan()

def part2(instructions: list[Instruction]) -> int:
    ship = Ship(0, 0, 0, 0, 0)
    waypoint = Waypoint(10, 0, 0, 1)
    for instruction in instructions:
        if instruction.direction == "R" or instruction.direction == "L":
            waypoint.rotate(instruction.direction, instruction.amount)
        elif instruction.direction == "F":
            for _ in range(instruction.amount):
                ship.move_to_waypoint(waypoint)
        else:
            waypoint.update(instruction.direction, instruction.amount)
    return ship.manhattan()


data = get_input()
print(f"Part 1: {part1(data)}")
print(f"Part 2: {part2(data)}")
