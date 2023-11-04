with open('2015\Day 2\Input.in') as file:
    data = [i for i in file.read().strip().split("\n")]

length = 0
width = 0
height = 0

sqfeet = 0

paper = 0

for item in data:
    dim = item.split("x")

    dim = [int(x) for x in dim]

    length = dim[0]
    width = dim[1]
    height = dim[2]

    dim.sort()

    sqfeet = 2*length*width + 2*width*height + 2*height*length + dim[0] * dim[1]

    paper += sqfeet
print(paper)