def process_input(file: str):
    with open(file) as f:
        dots, folds = f.read().split("\n\n")

    dots = sorted([list(map(int, item.split(","))) for item in dots.split("\n")])

    x_max = max((x for x, y in dots))
    y_max = max((y for x, y in dots))

    folds = [fold.strip("fold along ") for fold in folds.split("\n")]
    folds = [item.split("=") for item in folds]
    folds = [[axis, int(value)] for axis, value in folds]

    return dots, x_max, y_max, folds


def fold_paper(dots, folds):
    if folds[0] == "x":
        print("x")
    else:
        print("y")


def part_one(filename: str):
    dots, x_max, y_max, folds = process_input(filename)
    fold_paper(dots, folds[0])


input_file = "./test_input.txt"
print(f"Part One: {part_one(input_file)}")