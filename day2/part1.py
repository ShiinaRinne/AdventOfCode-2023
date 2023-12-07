with open("day2/input.txt") as f:
    games = f.readlines()

result = []
sum = 0
for game in games:
    game_index, pieces = game.split(":")
    game_index_int = int(game_index.split(" ")[1])

    pieces = pieces.replace("\n", "")
    use = True
    for piece in pieces.split(";"):
        piece = piece.strip()

        for i in piece.split(","):
            count, color = i.strip().split(" ")
            match color:
                case "blue":
                    max_count = 14
                case "green":
                    max_count = 13
                case "red":
                    max_count = 12

            if int(count) > max_count:
                use = False
                break
        if not use:
            break

    if use:
        result.append([game_index, pieces])
        sum += int(game_index.split(" ")[1])

[print(i) for i in result]

print(sum)
