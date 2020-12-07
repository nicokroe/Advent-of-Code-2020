from pathlib import Path

def part1():
    input_path = Path(__file__).parent / "input.txt"
    f = input_path.open().readlines()
    bag = "shiny gold"
    bags = []
    i = 0
    while True:
        for line in f:
            if not line.startswith(bag) and bag in line:
                bags.append(" ".join(line.split()[:2]))
        try:
            bag = bags[i]
        except IndexError:
            bags = set(bags)
            return len(bags)
        i += 1

def rec_sum(start, bagprops):
    result = 0
    for bagprop in start:
        for k, v in bagprop.items():
            result += v
            try:
                result += v * rec_sum(bagprops[k], bagprops)
            except KeyError:
                pass
    return result

def part2():
    input_path = Path(__file__).parent / "input.txt"
    bagprops = {}
    result = 0
    for line in input_path.open().readlines():
        splits = line.strip("\n.").replace(" contain", ",").replace("bags", "").replace("bag", "").split(",")
        propslist = []
        for split in splits[1:]:
            props = {}
            if not "other" in split:
                amount = int(split[1])
                color = split[3:].strip()
                props[color] = amount
            if props:
                propslist.append(props)
                bagprops[splits[0].strip()] = propslist
    result = rec_sum(bagprops["shiny gold"], bagprops)
    return result

print(part1())
print(part2())