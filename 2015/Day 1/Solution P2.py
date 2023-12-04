data = list(open('2015\Day 1\Input.in').read())
floor = 0
x = 0
for i in data:
    x += 1
    if i == '(': floor += 1
    elif i == ')': floor -= 1
    if floor == -1: break
print(x)