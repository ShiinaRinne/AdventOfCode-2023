from typing import Dict

with open("day2/input.txt") as f:
    games = f.readlines()

result = []
sum = 0
for game in games:
    least_count: Dict[str, int] = {}
    game_index, pieces = game.split(":")
    game_index_int = int(game_index.split(" ")[1])

    pieces = pieces.replace("\n", "")
    for piece in pieces.split(";"):
        piece = piece.strip()

        for i in piece.split(","):
            count, color = i.strip().split(" ")
            least_count[color] = (
                int(count)
                if color not in least_count.keys() or least_count[color] < int(count)
                else least_count[color]
            )

    print(f"{game_index_int} {least_count}")

    a = 1
    for value in least_count.values():
        a *= value
    sum += a

print(sum)
