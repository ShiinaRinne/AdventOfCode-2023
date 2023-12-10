with open("day3/input.txt") as f:
    lines = f.readlines()


symbols = "0123456789."
rows = "".join(lines).strip().split("\n")


def is_adjacent_to_symbol(row, number_start, number_end):
    for i in range(max(0, number_start - 1), min(len(row), number_end + 1 + 1)):
        if row[i] not in symbols:
            return True
    return False


total_sum = 0
for i, row in enumerate(rows):
    number = ""
    for j, char in enumerate(row):
        if char.isdigit():
            number += char
            if j == len(row) - 1 or not row[j + 1].isdigit():
                number_start = j - len(number) + 1
                number_end = j
                if any(is_adjacent_to_symbol(rows[k], number_start, number_end) for k in range(max(0, i - 1), min(len(rows), i + 1 + 1))):
                    total_sum += int(number)
                number = ""
        else:
            number = ""

print(total_sum)
