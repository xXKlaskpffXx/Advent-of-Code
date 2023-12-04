data = list(open('2015\Day 1\Input.in').read())
floor = 0
for i in data:
    if i == '(': floor += 1
    elif i == ')': floor -= 1
print(floor)