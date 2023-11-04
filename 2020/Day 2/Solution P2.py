with open('2020\Day 2\Input.in') as file:
    data = [i for i in file.read().strip().split("\n")]

policies = ["", "", "", ""]
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
            policies[2] = policy
            switch = 1
        elif switch == 1:
            policies[3] = policy
            switch = 0
    for value in policies[2].split(" "):
        if switch2 == 0:
            policies[1] = value
            switch2 = 1
        elif switch2 == 1:
            policies[2] = value
            switch2 = 0
    for policyValue in policies[1].split("-"):
        if switch3 == 0:
            policies[0] = policyValue
            switch3 = 1
        elif switch3 == 1:
            policies[1] = policyValue
            switch3 = 0
    password = list(policies[3])
    print(policies)
    if password[int(policies[0]) - 1] == policies[2] and password[int(policies[1]) - 1] != policies[2]:
        result += 1
    elif password[int(policies[0]) - 1] != policies[2] and password[int(policies[1]) - 1] == policies[2]:
        result += 1

print(result)