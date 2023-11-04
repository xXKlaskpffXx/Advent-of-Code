with open('2020\Day 1\Input.in') as file:
    data = [i for i in file.read().strip().split("\n")]

num = ""
result = 0

for item in data:
    for i in range(len(data)):
        if int(item) + int(data[i]) < 2020:
            if str(2020 - (int(item) + int(data[i]))) in data:
                result = int(item) * int(data[i]) * int(2020 - (int(item) + int(data[i])))

print(result)