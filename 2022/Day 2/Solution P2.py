with open('2022\Day 2\Input.in') as file:
    data = [i for i in file.read().strip().split("\n")]


setState = ""
opponent = ""
me = ""
points = 0

for item in data:
    game = item.split(" ")
    for item in game:
        if item == "X":
            setState = "lose"
        elif item == "Y":
            setState = "draw"
        elif item == "Z":
            setState = "win"
        elif item == "A":
            opponent = "R"
        elif item == "B":
            opponent = "P"
        elif item == "C":
            opponent = "S"
    if setState == "draw":
        me = opponent
    elif opponent == "R":
        if setState == "lose":
            me = "S"
        elif setState == "win":
            me = "P"
    elif opponent == "P":
        if setState == "lose":
            me = "R"
        elif setState == "win":
            me = "S"
    elif opponent == "S":
        if setState == "lose":
            me = "P"
        elif setState == "win":
            me = "R"

    #points for state
    if setState == "win":
        points += 6
    elif setState == "draw":
        points += 3

    #points for RPS
    if me == "R":
        points += 1
    elif me == "P":
        points += 2
    elif me == "S":
        points += 3    

print(points)