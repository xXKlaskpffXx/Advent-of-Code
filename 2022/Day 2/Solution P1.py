with open('2022\Day 2\Input.in') as file:
    data = [i for i in file.read().strip().split("\n")]

state = ""
me = ""
opponent = ""
points = 0


#RPS
for item in data:
    game = item.split(" ")
    for item in game:
        if item == "A":
            opponent = "R"
        elif item == "B":
            opponent = "P"
        elif item == "C":
            opponent = "S"
        elif item == "X":
            me = "R"
        elif item == "Y":
            me = "P"
        elif item == "Z":
            me = "S"
    #state
    if opponent == me:
        state = "draw"
    elif opponent == "R":
        if me == "P":
            state = "won"
        elif me == "S":
            state = "lost"
    elif opponent == "P":
        if me == "R":
            state = "lost"
        elif me == "S":
            state = "won"
    elif opponent == "S":
        if me == "R":
            state = "won"
        elif me == "P":
            state = "lost"

    #points for state
    if state == "won":
        points += 6
    elif state == "draw":
        points += 3

    #points for RPS
    if me == "R":
        points += 1
    elif me == "P":
        points += 2
    elif me == "S":
        points += 3    





print(points)