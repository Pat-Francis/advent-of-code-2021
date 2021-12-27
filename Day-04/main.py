def part_one(file: str) -> int:
    with open(file) as f:
        data = f.read().splitlines()
        numbers_to_call = [int(i) for i in data[0].split(",")]
        boards = []

        for i in range(2, len(data), 6):
            boards.append([list(map(int, d.split())) for d in data[i:i + 5]])

        for i in range(5, len(numbers_to_call)):
            check_rows = check_rows_for_bingo(numbers_to_call[0:i], boards)
            check_columns = check_columns_for_bingo(numbers_to_call[0:i], boards)
            if check_rows:
                score = calculate_score(check_rows[1], check_rows[2])
                return score
            elif check_columns:
                score = calculate_score(check_columns[1], check_columns[2])
                return score


def check_rows_for_bingo(numbers_called: list, boards: list) -> tuple:
    for board in boards:
        for row in board:
            if set(row).issubset(numbers_called):
                calculate_score(numbers_called, board)
                return True, numbers_called, board


def check_columns_for_bingo(numbers_called: list, boards: list) -> tuple:
    for board in boards:
        transposed_board = [[row[i] for row in board] for i in range(len(boards[0]))]
        for row in transposed_board:
            if set(row).issubset(numbers_called):
                calculate_score(numbers_called, board)
                return True, numbers_called, board


def calculate_score(numbers_called: list, winning_board: list) -> int:
    score = numbers_called[-1] * sum([num for row in winning_board for num in row if num not in numbers_called])
    return score


input_file = "./input.txt"
print(f"Part One: {part_one(input_file)}")
