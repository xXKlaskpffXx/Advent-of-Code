import re

with open('2022\Day 3\Input.in') as file:
    data = [i for i in file.read().strip().split("\n")]
with open('2022\Day 3\priorities.data') as file:
    data2 = [i for i in file.read().strip().split("\n")]

sum = 0

def get_priority(char):
    for item in data2:
        if char in item:
            return re.sub('[^0-9]', '', item)
                    


#Inspiriert
i = 0
while i < len(data):
    group = data[i: i + 3]
    v1 = list(group[0])
    v2 = list(group[1])
    v3 = list(group[2])
    for item in v1:
        if item in v2 and item in v3:
            commonItem = item
    sum += int(get_priority(commonItem))
    i += 3
print(sum)
