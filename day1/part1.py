with open("./day1/input.txt", 'r') as f:
    lines = f.readlines()
    

sum = 0
for line in lines:
    line = line.strip()
    first = -1
    last = -1
    for s in line:
        if(s.isdigit()):
            first = int(s)
            break
    for s in line[::-1]:
        if(s.isdigit()):
            last = int(s)
            break
    sum += first*10 + last
    print(f"line: {line}, num: {first*10 + last}")


print(sum)