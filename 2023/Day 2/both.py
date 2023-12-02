data = open("2023\Day 2\Input.in").read().split('\n')
CHARS = [' ',',',';',':']
COLORS = ['red','green','blue']
MAXCUBS = [12,13,14]
color = ''

gamenum = 1
game2 = []
gamesum = 0
switch = False
value = ''

for i in data:
    value = ''
    value2 = 0
    game2.clear()
    game = list(i)[8:]
    for j in game:
        if not j in CHARS: game2.append(j)
    for k in game2:
        if k.isnumeric():
            if color == COLORS[0] and value2 > MAXCUBS[0]:
                switch = True
            elif color == COLORS[1] and value2 > MAXCUBS[1]:
                switch = True
            elif color == COLORS[2] and value2 > MAXCUBS[2]:
                switch = True
            value += k
            value2 = int(value)
            color = ''
        else: 
            color += k
            value = ''
    if color == COLORS[0] and value2 > MAXCUBS[0]:
        switch = True
    elif color == COLORS[1] and value2 > MAXCUBS[1]:
        switch = True
    elif color == COLORS[2] and value2 > MAXCUBS[2]:
        switch = True
    if switch == False:
        gamesum += gamenum
    else: switch = False
    gamenum +=1
print(f"Part 1: {gamesum}")

mincubes = [0,0,0]
color = ''

gamenum = 1
game2 = []
gamesum = 0
switch = False
value = ''

def multiply(x):
    y = 1
    for i in range(len(x)):
        y *= x[i]
    return y

def clearvec(x):
    for i in range(len(x)):
        x[i] = 0
    return x

for i in data:
    value = ''
    value2 = 0
    game2.clear()
    game = list(i)[8:]
    for j in game:
        if not j in CHARS: game2.append(j)
    for k in game2:
        if k.isnumeric():
            if color == COLORS[0] and value2 > mincubes[0]:
                mincubes[0] = value2
            elif color == COLORS[1] and value2 > mincubes[1]:
                mincubes[1] = value2
            elif color == COLORS[2] and value2 > mincubes[2]:
                mincubes[2] = value2
            value += k
            value2 = int(value)
            color = ''
        else: 
            color += k
            value = ''
    if color == COLORS[0] and value2 > mincubes[0]:
        mincubes[0] = value2
    elif color == COLORS[1] and value2 > mincubes[1]:
        mincubes[1] = value2
    elif color == COLORS[2] and value2 > mincubes[2]:
        mincubes[2] = value2
    gamesum += multiply(mincubes)
    mincubes = clearvec(mincubes)
print(f"Part 2: {gamesum}")