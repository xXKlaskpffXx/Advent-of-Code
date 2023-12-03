data = open('2023\Day 3\Input.in').read().split('\n')
characters = [[],[]]
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

def writevalue(list, x, y, val):
    list[0].append(x-1)
    list[1].append(y)
    list[2].append(val)
    return list, 0

def writecharacter(list, x, y):
    list[0].append(x)
    list[1].append(y)
    return list


for i in data:
    for j in list(i):
        if not j == '.':
            if j.isnumeric():
                value = int(str(value) + j)
            else:
                characters = writecharacter(characters, x, y)
                if not value == 0: values, value = writevalue(values, x, y, value)
        else:
            if not value == 0: values, value = writevalue(values, x, y, value)
        x += 1
    if not value == 0: values, value = writevalue(values, x, y, value)
    x = 0
    y += 1
y = 0


for i in range(len(values[2])):
    for j in range(len(characters[0])):
        if checkifvalid(values[0][i], values[1][i], characters[0][j], characters[1][j], values[2][i]): 
            sum += values[2][i]
            break

print(sum)