from typing import List
from functools import reduce

with open("day3/input.txt") as f:
    lines = f.readlines()

symbols = "*"
rows = "".join(lines).strip().split("\n")


def find_adjacent_number(row: str, star_index) -> List[int] | None:
    number = []
    for i in range(max(0, star_index - 1), min(len(row), star_index + 1 + 1)):
        j = i
        if row[i].isdigit():
            while 0 <= j < len(row) and row[j].isdigit():
                if j == star_index:
                    number.append(row[j])
                    break

                if j < len(row):
                    number.insert(0, row[j]) if i - star_index <= 0 else number.append(row[j])
                    j += i - star_index
                else:
                    break
        if row[i] == "*" or (i == star_index and not row[i].isdigit()):
            number.append("*")  # special case. two numbers in one line, e.g. 862.766("*"'s index is same with "."), 862*766

    if len(number) != 0:
        t = "".join(number)
        a = t.split("*")
        return [int(s) for s in a if s.isdigit()]
    return None


total_sum = 0
for i, row in enumerate(rows):
    number = ""
    for j, char in enumerate(row):
        if char == "*":
            find_num = []
            for k in range(max(0, i - 1), min(len(rows), i + 1 + 1)):
                if (find_num_t := find_adjacent_number(rows[k], j)) != None:
                    find_num.extend(find_num_t)
                else:
                    continue

            if len(find_num) >= 2:
                result = reduce(lambda x, y: x * y, find_num)
                print(f"line{i+1}: findnum: {str(find_num):<12}", end="")
                print(f" {total_sum:<8} + {result:<6} => {total_sum+result}")
                total_sum += result


print(f"result: {total_sum}")
