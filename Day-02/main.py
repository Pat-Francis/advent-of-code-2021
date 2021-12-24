def part_one(file: str) -> int:
    with open(file) as f:
        instructions = [[j, int(k)] for j, k in [i.split() for i in f.read().splitlines()]]

        forward = sum([i[1] for i in instructions if i[0] == "forward"])
        down = sum([i[1] for i in instructions if i[0] == "down"])
        up = sum([i[1] for i in instructions if i[0] == "up"])

        product = forward * (down - up)
        return product


input_file = "./input.txt"
print(f"Part One: {part_one(input_file)}")
