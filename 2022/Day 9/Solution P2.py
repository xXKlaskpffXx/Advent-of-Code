with open('2022\Day 9\Input.in') as file:
    data = [i for i in file.read().strip().split("\n")]


Hx = 0
Hy = 0
Tx = 0
Ty = 0

tail_visited = []
Tailx = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
Taily = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for item in data:
    for i in range(int(item.split(" ")[1])):

        


        if item.split(" ")[0] == "R":
            Hx += 1
        elif item.split(" ")[0] == "L":
            Hx -= 1
        elif item.split(" ")[0] == "U":
            Hy += 1
        elif item.split(" ")[0] == "D":
            Hy -= 1

        Tailx[0] = Hx
        Taily[0] = Hy


        for i in range(9):
            Tx = Tailx[i + 1]
            Ty = Taily[i + 1]

            if Tailx[i] >= Tx + 2 and Taily[i] == Ty:
                Tx += 1
            elif Tailx[i] <= Tx - 2 and Taily[i] == Ty:
                Tx -= 1
            elif Taily[i] >= Ty + 2 and Tailx[i] == Tx:
                Ty += 1
            elif Taily[i] <= Ty - 2 and Tailx[i] == Tx:
                Ty -= 1
            elif Tailx[i] >= Tx + 1 and Taily[i] >= Ty + 2:
                Tx += 1
                Ty += 1
            elif Tailx[i] >= Tx + 2 and Taily[i] >= Ty + 1:
                Tx += 1
                Ty += 1
            elif Tailx[i] <= Tx - 1 and Taily[i] >= Ty + 2:
                Tx -= 1
                Ty += 1
            elif Tailx[i] <= Tx - 2 and Taily[i] >= Ty + 1:
                Tx -= 1
                Ty += 1
            elif Tailx[i] >= Tx + 1 and Taily[i] <= Ty - 2:
                Tx += 1
                Ty -= 1
            elif Tailx[i] >= Tx + 2 and Taily[i] <= Ty - 1:
                Tx += 1
                Ty -= 1
            elif Tailx[i] <= Tx - 1 and Taily[i] <= Ty - 2:
                Tx -= 1
                Ty -= 1
            elif Tailx[i] <= Tx - 2 and Taily[i] <= Ty - 1:
                Tx -= 1
                Ty -= 1
            Tailx[i + 1] = Tx
            Taily[i + 1] = Ty

        if (str(Tailx[9]) + " " + str(Taily[9])) not in tail_visited:
            tail_visited.append(str(Tailx[9]) + " " + str(Taily[9]))

    #print("Hx: " + str(Hx))
    #print("Hy: " + str(Hy) + "\n")
    #print("Tailx: " + str(Tailx))
    #print("Taily: " + str(Taily) + "\n")
    
print(len(tail_visited))