with open('2022\Day 4\Input.in') as file:
    data = [i for i in file.read().strip().split("\n")]



switch = 0
lastNum = 0

assignment = [0, 0, 0, 0]

partiallyContaining = 0


for item in data:
    for section in item.split(","):
        for sectionnum in section.split("-"):
            if switch == 0:
                assignment[0] = int(sectionnum)
                switch = 1
            elif switch == 1:
                assignment[1] = int(sectionnum)
                switch = 2
            elif switch == 2:
                assignment[2] = int(sectionnum)
                switch = 3
            elif switch == 3:
                assignment[3] = int(sectionnum)
                switch = 0
    if assignment[1] >= assignment[2] and assignment[0] <= assignment[2] and assignment[3] >= assignment[1]:
        partiallyContaining += 1
    elif assignment[0] <= assignment[2] and assignment[1] >= assignment[3]:
        partiallyContaining += 1
    elif assignment[0] >= assignment[2] and assignment[1] <= assignment[3]:
        partiallyContaining += 1
    elif assignment[3] >= assignment[0] and assignment[2] <= assignment[0]:
        partiallyContaining += 1
print(partiallyContaining)
