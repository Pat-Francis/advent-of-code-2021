def process_input(file: str) -> list[list[tuple]]:
    with open(file) as f:
        data = list(map(lambda line: line.strip().split(" | "), f.readlines()))
        lines = [[tuple(map(str, line[0].split())), tuple(map(str, line[1].split()))] for line in data]
        return lines


def part_one(filename: str) -> int:
    lines = process_input(input_file)
    num_of_segments = [2, 3, 4, 7]
    return len([val for tup in [i[1] for i in lines] for val in tup if len(val) in num_of_segments])


input_file = "./input.txt"
print(f"Part One: {part_one(input_file)}")
