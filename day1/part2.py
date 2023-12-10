from typing import Dict, List

num_dict: Dict[str,int] = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}
with open("./day1/input.txt", 'r') as f:
    lines = f.readlines()
    

sum = 0
for line in lines:
    line = line.strip().lower()
    
    line_str = ""
    line_nums:List[int] = []
    for char in line:
        if char.isdigit():
            line_nums.append(int(char))
            continue
        
        line_str += char
        for k, v in num_dict.items():
            if line_str.endswith(k):
                line_nums.append(v)
                
    print(f"{line} => {line_nums}")
    sum += line_nums[0] * 10 + line_nums[-1]   
            
print(sum)