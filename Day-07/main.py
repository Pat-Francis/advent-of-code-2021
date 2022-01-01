def process_input(file: str) -> list[int]:
    with open(file) as f:
        data = sorted(list(map(int, f.read().split(","))))
        return data


def part_one(filename: str) -> int:
    data = process_input(input_file)
    median = data[len(data) // 2]
    fuel_cost = sum([abs(x - median) for x in data])

    return fuel_cost


input_file = "./input.txt"
print(f"Part One: {part_one(input_file)}")
