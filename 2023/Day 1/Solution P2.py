data = open("2023\Day 1\Input.in").read().split('\n')
sum = 0
digitsl = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
digitsn = ["1","2","3","4","5","6","7","8","9"]
digitsl_inverted = ["eno", "owt", "eerht", "ruof", "evif", "xis", "neves", "thgie", "enin"]

fstnum = 0
lstnum = 0

def istnumericV(x):
    y = ''
    i = -1
    for j in range(len(list(x))+1):
        i += 1
        if digitsl[0] in x[0:i] or digitsn[0] in x[0:i]: 
            return '1'
        if digitsl[1] in x[0:i] or digitsn[1] in x[0:i]: 
            return '2'
        if digitsl[2] in x[0:i] or digitsn[2] in x[0:i]: 
            return '3'
        if digitsl[3] in x[0:i] or digitsn[3] in x[0:i]: 
            return '4'
        if digitsl[4] in x[0:i] or digitsn[4] in x[0:i]: 
            return '5'
        if digitsl[5] in x[0:i] or digitsn[5] in x[0:i]: 
            return '6'
        if digitsl[6] in x[0:i] or digitsn[6] in x[0:i]: 
            return '7'
        if digitsl[7] in x[0:i] or digitsn[7] in x[0:i]: 
            return '8'
        if digitsl[8] in x[0:i] or digitsn[8] in x[0:i]: 
            return '9'
            

def istnumericR(x):
    y = ''
    i = -1
    x = x[::-1]
    for j in range(len(list(x))+1):
        i += 1
        if digitsl_inverted[0] in x[0:i] or digitsn[0] in x[0:i]: 
            return '1'
        if digitsl_inverted[1] in x[0:i] or digitsn[1] in x[0:i]: 
            return '2'
        if digitsl_inverted[2] in x[0:i] or digitsn[2] in x[0:i]: 
            return '3'
        if digitsl_inverted[3] in x[0:i] or digitsn[3] in x[0:i]: 
            return '4'
        if digitsl_inverted[4] in x[0:i] or digitsn[4] in x[0:i]: 
            return '5'
        if digitsl_inverted[5] in x[0:i] or digitsn[5] in x[0:i]: 
            return '6'
        if digitsl_inverted[6] in x[0:i] or digitsn[6] in x[0:i]: 
            return '7'
        if digitsl_inverted[7] in x[0:i] or digitsn[7] in x[0:i]: 
            return '8'
        if digitsl_inverted[8] in x[0:i] or digitsn[8] in x[0:i]: 
            return '9'

for i in data:
    fstnum = istnumericV(i)
    lstnum = istnumericR(i)
    num = fstnum + lstnum
    sum += int(num)
print(sum)