with open('2022\Day 8\Input.in') as file:
    data = [i for i in file.read().strip().split("\n")] 

current_x = 0
current_y = 0

trees = [""]
visible = []

length = len(data) - 1
width = len(data[0]) - 1



for item in data:
    for crnt_item in list(item):
        trees.append(str(current_x) + " " + str(current_y) + " " + crnt_item)
        current_x += 1
    current_x = 0
    current_y += 1

def check_if_visible(x, y, height):
    visible.append(x + " " + y + " " + height)
    indicator1 = 0
    indicator2 = 0
    indicator3 = 0
    indicator4 = 0
    for item in trees[1:]:
        chunk = item.split(" ")
        print(chunk)
        if chunk[0] == x and chunk[1] < y and chunk[2] >= height:
            indicator1 = 1
        if chunk[0] == x and chunk[1] > y and chunk[2] >= height:
            indicator2 = 1
        if chunk[0] < x and chunk[1] == y and chunk[2] >= height:
            indicator3 = 1
        if chunk[0] > x and chunk[1] == y and chunk[2] >= height:
            indicator4 = 1
    if indicator1 == 1 and indicator2 == 1 and indicator3 == 1 and indicator4 == 1:
        visible.remove(x + " " + y + " " + height)
    print(str(indicator1) + " " + str(indicator2) + " " + str(indicator3) + " " + str(indicator4) + " " + x + " " + y)

for item in trees[1:]:
    chunk = item.split(" ")
    if int(chunk[0]) != 0 and int(chunk[0]) != width and int(chunk[1]) != 0 and int(chunk[1]) != length:
        check_if_visible(chunk[0], chunk[1], chunk[2])
print(visible)
print(len(visible) + width*2 + length*2)

