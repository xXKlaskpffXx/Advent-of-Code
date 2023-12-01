data = open("2023\Day 1\Input.in").read().split('\n')
sum = 0
letters = ""
digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def istnumeric(x):
    if x == 'one':
        return 1
    elif x == 'two':
        return 2
    elif x == 'three':
        return 3
    elif x == 'four':
        return 4
    elif x == 'five':
        return 5
    elif x == 'six':
        return 6
    elif x == 'seven':
        return 7
    elif x == 'eight':
        return 8
    elif x == 'nine':
        return 9

for i in data:
    for j in list(i):
        if j.isnumeric():
            letters = ""
            fstnum = j
            new_list = i[::-1]
            for k in new_list:
                if k.isnumeric():
                    letters = ""
                    lstnum = k
                else:
                    letters = k + letters
                    if letters in digits:
                        fstnum = istnumeric(letters) 
        else:
            letters += j
            if letters in digits:
                fstnum = istnumeric(letters)

    justkidding = lstnum + fstnum
    print(justkidding)
    sum += int(justkidding)
print(sum)