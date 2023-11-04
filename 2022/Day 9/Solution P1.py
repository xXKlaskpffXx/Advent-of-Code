with open('2022\Day 9\Input.in') as file:
    data = [i for i in file.read().strip().split("\n")]


Hx = 0
Hy = 0
Tx = 0
Ty = 0

tail_visited = []
tail = []

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
        if Hx >= Tx + 2 and Hy == Ty:
            Tx += 1
        elif Hx <= Tx - 2 and Hy == Ty:
            Tx -= 1
        elif Hy >= Ty + 2 and Hx == Tx:
            Ty += 1
        elif Hy <= Ty - 2 and Hx == Tx:
            Ty -= 1
        elif Hx >= Tx + 1 and Hy >= Ty + 2:
            Tx += 1
            Ty += 1
        elif Hx >= Tx + 2 and Hy >= Ty + 1:
            Tx += 1
            Ty += 1
        elif Hx <= Tx - 1 and Hy >= Ty + 2:
            Tx -= 1
            Ty += 1
        elif Hx <= Tx - 2 and Hy >= Ty + 1:
            Tx -= 1
            Ty += 1
        elif Hx >= Tx + 1 and Hy <= Ty - 2:
            Tx += 1
            Ty -= 1
        elif Hx >= Tx + 2 and Hy <= Ty - 1:
            Tx += 1
            Ty -= 1
        elif Hx <= Tx - 1 and Hy <= Ty - 2:
            Tx -= 1
            Ty -= 1
        elif Hx <= Tx - 2 and Hy <= Ty - 1:
            Tx -= 1
            Ty -= 1

        if (str(Tx) + " " + str(Ty)) not in tail_visited:
            tail_visited.append(str(Tx) + " " + str(Ty))

    #print("Hx: " + str(Hx))
    #print("Hy: " + str(Hy) + "\n")
    #print("Tx: " + str(Tx))
    #print("Ty: " + str(Ty) + "\n")
    
print(len(tail_visited))