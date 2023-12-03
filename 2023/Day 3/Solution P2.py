data = open('2023\Day 3\Input.in').read().split('\n')
characters = [[],[],[]]
values = [[],[],[]]
x = 0
y = 0
value = 0

sum = 0

def checkifvalidgear(x, y, vals):
    p = 0
    product = 1
    for i in range(len(vals[0])):
        dx = (vals[0][i] - x)
        dy = (vals[1][i] - y)
        if (dx <= 1 and dx >= -1) or ((dx - len(list(str(vals[2][i]))) + 1) <= 1 and (dx - len(list(str(vals[2][i]))) + 1) >= -1):
            if dy <= 1 and dy >= -1:
                p += 1
                product *= vals[2][i]
    if p == 2:
        return True, product
    return False, 0


def writevalue(list, x, y, val):
    list[0].append(x-1)
    list[1].append(y)
    list[2].append(val)
    return list, 0

def writecharacter(list, x, y, gear):
    list[0].append(x)
    list[1].append(y)
    list[2].append(gear)
    return list


#storing the values and chars
for i in data:
    for j in list(i):
        if not j == '.':
            if j.isnumeric():
                value = int(str(value) + j)
            else:
                if j == '*':
                    characters = writecharacter(characters, x, y, True)
                else:
                    characters = writecharacter(characters, x, y, False)
                if not value == 0: values, value = writevalue(values, x, y, value)
        else:
            if not value == 0: values, value = writevalue(values, x, y, value)
        x += 1
    if not value == 0: values, value = writevalue(values, x, y, value)
    x = 0
    y += 1
y = 0

#summing the gears
for i in range(len(characters[0])):
    if characters[2][i] == True:
        p, product = checkifvalidgear(characters[0][i], characters[1][i], values)
        if p:
            sum += product
        

print(sum)