data = open("2023\Day 1\Input.in").read().split('\n')
sum = 0
digitsl = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
digitsn = ["1","2","3","4","5","6","7","8","9"]

def istnumeric(x):
    y = ''
    z = ''
    i = -1
    for j in range(len(list(x))):
        i += 1
        if digitsl[0] in x[0:i] or digitsn[0] in x[0:i]: 
            y += '1'
            z = x[i:]
        if digitsl[1] in x[0:i] or digitsn[1] in x[0:i]: 
            y += '2'
            z = x[i:]
        if digitsl[2] in x[0:i] or digitsn[2] in x[0:i]: 
            y += '3'
            z = x[i:]
        if digitsl[3] in x[0:i] or digitsn[3] in x[0:i]: 
            y += '4'
            z = x[i:]
        if digitsl[4] in x[0:i] or digitsn[4] in x[0:i]: 
            y += '5'
            z = x[i:]
        if digitsl[5] in x[0:i] or digitsn[5] in x[0:i]: 
            y += '6'
            z = x[i:]
        if digitsl[6] in x[0:i] or digitsn[6] in x[0:i]: 
            y += '7'
            z = x[i:]
        if digitsl[7] in x[0:i] or digitsn[7] in x[0:i]: 
            y += '8'
            z = x[i:]
        if digitsl[8] in x[0:i] or digitsn[8] in x[0:i]: 
            y += '9'
            z = x[i:]
        x = z
        i = 0
    return y

for i in data:
    print(istnumeric(i))