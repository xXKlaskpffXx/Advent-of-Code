data = open('2023\Day 3\Input.in').read().split('\n')
zeichen = [[],[]]
values = [[],[],[]]
x = 0
y = 0
value = 0

sum = 0

def checkifvalid(valx, valy, zx, zy, val):
    dx = valx - zx
    dy = valy - zy
    if dx <= len(list(str(val))) and dx >= -1:
        if dy <= 1 and dy >= -1:
            return True



for i in data:
    for j in list(i):
        if not j == '.':
            if j.isnumeric():
                value = int(str(value) + j)
            else:
                zeichen[0].append(x)
                zeichen[1].append(y)
                if not value == 0: 
                    values[0].append(x-1)
                    values[1].append(y)
                    values[2].append(value)
                    value = 0
        else:
            if not value == 0: 
                values[0].append(x-1)
                values[1].append(y)
                values[2].append(value)
                value = 0
        x += 1
    x = 0
    y += 1
y = 0


for i in range(len(values[2])):
    for j in range(len(zeichen[0])):
        if checkifvalid(values[0][i], values[1][i], zeichen[0][j], zeichen[1][j], values[2][i]): 
            sum += values[2][i]
            break

print(sum)