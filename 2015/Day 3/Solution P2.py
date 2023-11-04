with open('2015\Day 3\Input.in') as file:
    data = [i for i in file.read().strip()]

operations = list(data)

SantaX = 0
SantaY = 0
RoboSantaX = 0
RoboSantaY = 0

switch = 0

SantaHouse = ""
RoboSantaHouse = ""

delivered = []

for item in operations:
    if item == "^":
        if switch == 0:
            SantaY += 1
        else:
            RoboSantaY += 1
    elif item == "v":
        if switch == 0:
            SantaY -= 1
        else:
            RoboSantaY -= 1
    elif item == "<":
        if switch == 0:
            SantaX -= 1
        else:
            RoboSantaX -= 1
    elif item == ">":
        if switch == 0:
            SantaX += 1
        else:
            RoboSantaX += 1

    SantaHouse = SantaX, SantaY
    RoboSantaHouse = RoboSantaX, RoboSantaY

    if not SantaHouse in delivered:
        delivered.append(SantaHouse)
    if not RoboSantaHouse in delivered:
        delivered.append(RoboSantaHouse)

    if switch == 0:
        switch = 1
    elif switch == 1:
        switch = 0
    
    

print(len(delivered))