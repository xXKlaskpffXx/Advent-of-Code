with open('2015\Day 3\Input.in') as file:
    data = [i for i in file.read().strip()]

operations = list(data)

x = 0
y = 0

house = ""

delivered = []

for item in operations:
    if item == "^":
        y += 1
    elif item == "v":
        y -= 1
    elif item == "<":
        x -= 1
    elif item == ">":
        x += 1

    house = x, y
    
    if not house in delivered:
        delivered.append(house)

print(len(delivered) + 1)