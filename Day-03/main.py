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


def part_two(file: str) -> int:
    with open(file) as f:
        data = f.read().splitlines()
        oxygen_rating = data
        co2_rating = data

        for i in range(len(data[0])):
            oxy_digits = [d[i] for d in oxygen_rating]
            most_common = '0' if oxy_digits.count('0') > oxy_digits.count('1') else '1'
            oxygen_rating = [j for j in oxygen_rating if j[i] == most_common]
            if len(oxygen_rating) == 1:
                break

        for i in range(len(data[0])):
            co2_digits = [d[i] for d in co2_rating]
            most_common = '0' if co2_digits.count('0') > co2_digits.count('1') else '1'
            co2_rating = [j for j in co2_rating if j[i] != most_common]
            if len(co2_rating) == 1:
                break

        product = int(oxygen_rating[0], 2) * int(co2_rating[0], 2)
        return product


input_file = "./input.txt"
print(f"Part One: {part_one(input_file)}")
print(f"Part Two: {part_two(input_file)}")
