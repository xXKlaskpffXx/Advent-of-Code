with open('2015\Day 2\Input.in') as file:
    data = [i for i in file.read().strip().split("\n")]

length = 0
width = 0
height = 0

ribbon = 0

for item in data:
    dim = item.split("x")

    dim = [int(x) for x in dim]

    dim.sort()

    length = dim[0]
    width = dim[1]
    height = dim[2]
    ribbon += length*2 + width*2 + length*width*height

print(ribbon)