with open('2022\Day 6\Input.in') as file:
    data = list(file.read())

sequence = []
temp_sequence = []
lost = 0
switch = 0

print(len(data))

for inte in range(len(data)):
    sequence = data[inte-1:inte+13]
    for item in sequence:
        if sequence.count(item) >= 2:
            lost = 1
    if lost == 0:
        if switch < 2:
            print(inte + 13)
            print(sequence)
            switch += 1
    lost = 0