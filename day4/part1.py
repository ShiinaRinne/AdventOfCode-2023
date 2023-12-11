with open("day4/input.txt") as f:
    lines = f.readlines()
    
total_score = 0
for i, card in enumerate(lines):
    winning_numbers, self_numbers = map(set, map(str.split, card.split(":")[1].split("|")))
    self_winning_numbers = winning_numbers & self_numbers
    winning_count = len(self_winning_numbers)

    score = int(2**(winning_count-1))
    # print(f"{i} | Score: {score}, Winning numbers: {self_winning_numbers}, Winning count: {winning_count}, Winning numbers: {winning_numbers}, total numbers: {self_numbers}")
    total_score+=score
    
print(total_score)
