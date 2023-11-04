with open('2020\Day 2\Input.in') as file:
    data = [i for i in file.read().strip().split("\n")]

policies = ["", "", ""]
switch = 0
switch2 = 0
switch3 = 0

password = []

count = 0
result = 0

min = 0
max = 0

for item in data:
    for policy in item.split(": "):
        if switch == 0:
            policies[1] = policy
            switch = 1
        elif switch == 1:
            policies[2] = policy
            switch = 0
    for value in policies[1].split(" "):
        if switch2 == 0:
            policies[0] = value
            switch2 = 1
        elif switch2 == 1:
            policies[1] = value
            switch2 = 0
    for policyValue in policies[0].split("-"):
        if switch3 == 0:
            min = int(policyValue)
            switch3 = 1
            print("hi")
        elif switch3 == 1:
            max = int(policyValue)
            switch3 = 0
    password = list(policies[2])
    for c in password:
        if c == policies[1]:
            count += 1
    if count <= max and count >= min:
        result += 1
        
    count = 0
    print(policies[0], min, max)
print(result)