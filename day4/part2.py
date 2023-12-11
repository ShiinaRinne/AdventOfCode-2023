with open("day4/input.txt") as f:
    lines = f.readlines()
 
cards = [1]*len(lines)
for i, card in enumerate(lines):
    winning_numbers, self_numbers = map(set, map(str.split, card.split(":")[1].split("|")))
    self_winning_numbers = winning_numbers & self_numbers
    winning_count = len(self_winning_numbers)
    
    for j in range(1, winning_count + 1):
        cards[i + j] += cards[i]

print(sum(cards))
    
