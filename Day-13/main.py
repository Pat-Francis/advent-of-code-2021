def process_input(file: str):
    with open(file) as f:
        dots, folds = f.read().split("\n\n")

    dots = [list(map(int, item.split(","))) for item in dots.split("\n")]
    print(dots)
    x_max = max((x for x, y in dots))
    y_max = max((y for x, y in dots))

    folds = [fold.strip("fold along ") for fold in folds.split("\n")]
    folds = [item.split("=") for item in folds]
    folds = [[axis, int(value)] for axis, value in folds]

    return dots, x_max, y_max, folds


def fold_paper(dots, x_max, y_max, axis, value):
    new_dots = []
    if axis == "x":
        for x, y in dots:
            if x > value:
                new_dots.append((2 * value - x, y))
            else:
                new_dots.append((x, y))
        x_max = value - 1
    elif axis == "y":
        for x, y in dots:
            if y > value:
                new_dots.append((x, 2 * value - y))
            else:
                new_dots.append((x, y))
        y_max = value - 1
    dots = new_dots

    return dots, x_max, y_max


def part_one(filename: str):
    dots, x_max, y_max, folds = process_input(filename)
    for axis, value in folds:
        dots, x_max, y_max = fold_paper(dots, x_max, y_max, axis, value)
        break  # only first fold is required for part one

    return len(set(dots))


input_file = "./input.txt"
print(f"Part One: {part_one(input_file)}")