from statistics import median


def process_input(file: str) -> list[int]:
    with open(file) as f:
        data = sorted(list(map(int, f.read().split(","))))
        return data


def part_one(filename: str) -> int:
    data = process_input(filename)
    return int(sum([abs(x - median(data)) for x in data]))


def part_two(filename: str) -> int:
    data = process_input(filename)
    return min([sum([fuel_cost(x, r) for x in data]) for r in range(min(data), max(data) + 1)])


def fuel_cost(start, end: int) -> int:
    dist = abs(start - end)
    return int(dist * (dist + 1) / 2)


input_file = "./input.txt"
print(f"Part One: {part_one(input_file)}")
print(f"Part Two: {part_two(input_file)}")