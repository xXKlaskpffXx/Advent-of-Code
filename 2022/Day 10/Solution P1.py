cycle = 0
x = 1
ss_sum = 0

with open('2022\Day 10\Input.in') as file:
    data = [i for i in file.read().strip().split("\n")]


def compare(c, x, ss_s):
    if c == 20 or c == 60 or c == 100 or c == 140 or c == 180 or c == 220:
        ss_s += c * x
        print(f"strength: {c * x} sum: {ss_s}, cycle: {c}")
    return  ss_s

def addx(x, v, c, ss_sum):
    #cycle 1: do nothing
    c += 1
    ss_sum = compare(c, x, ss_sum)
    #cycle 2: do nothing
    c += 1
    ss_sum = compare(c, x, ss_sum)
    #end cycle 2: changed x
    c += 1
    x += v
    return x, c, ss_sum

def noop(c, x, ss_sum):
    c += 1
    ss_sum = compare(c, x, ss_sum)
    return c, ss_sum

for i in data:
    i = i.split(" ")
    if i[0] == "noop":
        cycle, ss_sum = noop(cycle, x, ss_sum)
    elif i[0] == "addx":
        x, cycle, ss_sum = addx(x, int(i[1]), cycle, ss_sum)
    else:
        print("error")