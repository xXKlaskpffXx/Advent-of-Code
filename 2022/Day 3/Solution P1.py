import re

with open('2022\Day 3\Input.in') as file:
    data = [i for i in file.read().strip().split("\n")]
with open('2022\Day 3\priorities.data') as file:
    data2 = [i for i in file.read().strip().split("\n")]


contents = ""
fhalf = ""
shalf = ""

ItemType = ""

sum = 0

def split_list(a_list):
    half = len(a_list)//2
    return a_list[:half], a_list[half:]

def get_priority(char):
    for item in data2:
        if char in item:
            return re.sub('[^0-9]', '', item)
                    

for item in data:
    contents = list(item)
    fhalf, shalf = split_list(contents)
    for item in fhalf:
        if item in shalf:
            ItemType = item
    sum += int(get_priority(ItemType))



print(sum)