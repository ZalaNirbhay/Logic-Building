num = 5
pattern = ""

def pattern_f(num, row):
    space = " " * (num-row)
    if row == 1:
        return space + "*" + '\n'
    else:
        middle_space = " " * (2*row - 3)
        return space + "*" + middle_space + "*" + '\n'


for row in range(1, num+1):
    pattern += pattern_f(num=num, row=row)

for row in range(num-1, 0, -1):
    pattern += pattern_f(num=num, row=row)
    

print(pattern)