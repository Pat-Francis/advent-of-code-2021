def part_one(filename: str) -> int:
    with open(filename) as f:
        instructions = [[j, int(k)] for j, k in [i.split() for i in f.read().splitlines()]]

        forward = sum([i[1] for i in instructions if i[0] == "forward"])
        down = sum([i[1] for i in instructions if i[0] == "down"])
        up = sum([i[1] for i in instructions if i[0] == "up"])

        product = forward * (down - up)
        return product


def part_two(filename: str) -> int:
    with open(filename) as f:
        instructions = [[j, int(k)] for j, k in [i.split() for i in f.read().splitlines()]]

        horizontal = 0
        depth = 0
        aim = 0

        for step in instructions:
            if step[0] == "forward":
                horizontal += step[1]
                if aim != 0:
                    depth += step[1] * aim
            elif step[0] == "down":
                aim += step[1]
            else:
                aim -= step[1]

        product = horizontal * depth
        return product


input_file = "./input.txt"
print(f"Part One: {part_one(input_file)}")
print(f"Part Two: {part_two(input_file)}")
