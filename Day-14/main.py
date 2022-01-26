from collections import defaultdict
from collections import Counter


def process_input(file: str):
    data = defaultdict(str)
    with open(file) as f:
        template, inserts = f.read().split("\n\n")

    split_inserts = [line.strip().split(" -> ") for line in inserts.splitlines()]

    for (pair, insert) in split_inserts:
        data[pair] += insert

    return template, data


def part_one(filename: str):
    template, data = process_input(filename)

    for j in range(10):
        new_template = ""
        for i in range(len(template) - 1):
            pair = f"{template[i]}{template[i + 1]}"
            insert = data[pair]
            new_template += f"{template[i]}{insert}"
        new_template += f"{template[-1]}"  # adds last character of template to new_template
        template = new_template
    else:
        counts = Counter(template)
        most_common = counts.most_common()[0][1]
        least_common = counts.most_common()[-1][1]

        return most_common - least_common


input_file = "./input.txt"
print(f"Part One: {part_one(input_file)}")