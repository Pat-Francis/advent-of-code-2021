def part_one(file: str) -> int:
    with open(file) as f:
        data = f.read().splitlines()
        gamma = ''

        for i in range(len(data[0])):
            digit = [int(d[i]) for d in data]
            gamma += f"{max(set(digit), key=digit.count)}"

        epsilon = ''.join(['1' if i == '0' else '0' for i in gamma])

        product = int(gamma, 2) * int(epsilon, 2)
        return product


input_file = "./input.txt"
print(f"Part One: {part_one(input_file)}")
