data = open("2023\Day 1\Input.in").read().split("\n")
sum = 0
letters = ""
digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def istnumeric(x):
    for i in range(len(list(x))):
        if digits[0] in x: return '1'    
        if digits[1] in x: return '2'
        if digits[2] in x: return '3'
        if digits[3] in x: return '4'
        if digits[4] in x: return '5'
        if digits[5] in x: return '6'
        if digits[6] in x: return '7'
        if digits[7] in x: return '8'
        if digits[8] in x: return '9'

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
                    break
                else:
                    letters = k + letters
                    if letters in digits:
                        lstnum = istnumeric(letters) 
                        break
        else:
            letters += j
            if letters in digits:
                fstnum = istnumeric(letters)
                break

    justkidding = lstnum + fstnum
    print(justkidding)
    sum += int(justkidding)
print(sum)