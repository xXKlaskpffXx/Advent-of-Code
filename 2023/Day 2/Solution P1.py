data = open("2023\Day 2\input.in").read().split('\n')
print(data)
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
    print(gamenum)
    if switch == False:
        gamesum += gamenum
    else: switch = False
    gamenum +=1
    print(gamesum)
print(gamesum)