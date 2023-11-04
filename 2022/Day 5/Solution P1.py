with open('2022\Day 5\Input.in') as file:
    data = [i for i in file.read().strip().split("\n")]

Stack1 = ["F", "C", "P", "G", "Q", "R"]
Stack2 = ["W", "T", "C", "P"]
Stack3 = ["B", "H", "P", "M", "C"]
Stack4 = ["L", "T", "Q", "S", "M", "P", "R"]
Stack5 = ["P", "H", "J", "Z", "V", "G", "N"]
Stack6 = ["D", "P", "J"]
Stack7 = ["L", "G", "P", "Z", "F", "J", "T", "R"]
Stack8 = ["N", "L", "H", "C", "F", "P", "T", "J"]
Stack9 = ["G", "V", "Z", "Q", "H", "T", "C", "W"]

Stacked = [Stack1, Stack2, Stack3, Stack4, Stack5, Stack6, Stack7, Stack8, Stack9]

operation = []

for item in data[10:]:
    for op in item.split(" "):
        if op != "move" and op != "from" and op != "to":
            operation.append(op)
    for i in range(int(operation[0])):
        Stacked[int(operation[2]) - 1].append(Stacked[int(operation[1]) - 1][len(Stacked[int(operation[1]) - 1]) - 1])
        Stacked[int(operation[1]) - 1].pop(-1)
    operation = []
print(Stacked[0][len(Stacked[0]) - 1], Stacked[1][len(Stacked[1]) - 1], Stacked[2][len(Stacked[2]) - 1], Stacked[3][len(Stacked[3]) - 1], Stacked[4][len(Stacked[4]) - 1], Stacked[5][len(Stacked[5]) - 1], Stacked[6][len(Stacked[6]) - 1], Stacked[7][len(Stacked[7]) - 1], Stacked[8][len(Stacked[8]) - 1])