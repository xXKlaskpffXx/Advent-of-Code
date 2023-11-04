with open('2022\Day 1\Input.in') as file:
    data = [i for i in file.read().strip().split("\n")]

max = 0
count = 0
for item in data:
    if item == '':
        count = 0
    else:
        num = int(item)
        count += num
    if count > max:
        max = count

print(max)
