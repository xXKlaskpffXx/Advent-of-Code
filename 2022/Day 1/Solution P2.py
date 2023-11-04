with open('2022\Day 1\Input.in') as file:
    data = [i for i in file.read().strip().split("\n")]

max = 0
max2 = 0
max3 = 0
count = 0
for item in data:
    if item == '':
        count = 0
    else:
        num = int(item)
        count += num
    if count > max:
        max = count
    elif count > max2:
        if count < max:
            max2 = count
    elif count > max3:
        if count < max2:
            max3 = count

print(max + max2 + max3)
