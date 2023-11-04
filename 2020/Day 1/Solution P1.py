with open('2020\Day 1\Input.in') as file:
    data = [i for i in file.read().strip().split("\n")]

num = ""
result = 0

for item in data:
    num = 2020 - int(item)
    if str(num) in data:
        result = int(item) * num

print(result)