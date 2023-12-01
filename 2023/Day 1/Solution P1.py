data = open("2023\Day 1\Input.in").read().split('\n')
sum = 0

for i in data:

    for j in list(i):
        if j.isnumeric():
            fstnum = j
            new_list = i[::-1]
            for k in new_list:
                if k.isnumeric():
                    lstnum = k
                    break
            

    justkidding = lstnum + fstnum
    print(justkidding)
    sum += int(justkidding)
print(sum)