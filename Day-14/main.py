from collections import Counter, defaultdict


def process_input(file: str):
    data = defaultdict(str)
    with open(file) as f:
        template, inserts = f.read().split("\n\n")

    split_inserts = [line.strip().split(" -> ") for line in inserts.splitlines()]

    for (pair, insert) in split_inserts:
        data[pair] += insert

    return template, data


def part_one(filename: str) -> int:
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


def part_two(filename: str) -> int:
    template, data = process_input(filename)
    pairs_count = Counter()
    total_count = Counter()

    # starting list of pairs from template
    for i in range(len(template) - 1):
        pair = f"{template[i]}{template[i + 1]}"
        pairs_count.update([pair])

    # add starting template to total_count
    for i in template:
        total_count.update(i)

    for i in range(40):
        new_pairs = Counter()
        for k, v in pairs_count.items():
            pair_one = f"{k[0]}{data[k]}"
            pair_two = f"{data[k]}{k[1]}"

            new_pairs[pair_one] += v
            new_pairs[pair_two] += v

            total_count[data[k]] += v

        pairs_count = new_pairs

    most_common = total_count.most_common()[0][1]
    least_common = total_count.most_common()[-1][1]
    return most_common - least_common


input_file = "./input.txt"
print(f"Part One: {part_one(input_file)}")
print(f"Part Two: {part_two(input_file)}")
