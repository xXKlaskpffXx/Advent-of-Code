with open('2021\Day 3\Input.in') as file:
    data = [i for i in file.read().strip().split("\n")]

bits = ""
gamma = 0
epsilon = 0
    
def getBit(n):


    ones = 0
    zeros = 0

    for item in data:
        bits = list(item)
        if bits[n] == "0":
            zeros += 1
        elif bits[n] == "1":
            ones += 1

    if zeros > ones:
        return 0
    elif ones > zeros:
        return 1
def geteBit(n):


    ones = 0
    zeros = 0

    for item in data:
        bits = list(item)
        if bits[n] == "0":
            zeros += 1
        elif bits[n] == "1":
            ones += 1

    if zeros > ones:
        return 1
    elif ones > zeros:
        return 0

byte = [getBit(0), getBit(1), getBit(2), getBit(3), getBit(4), getBit(5), getBit(6), getBit(7), getBit(8), getBit(9), getBit(10), getBit(11)]
ebyte = [geteBit(0), geteBit(1), geteBit(2), geteBit(3), geteBit(4), geteBit(5), geteBit(6), geteBit(7), geteBit(8), geteBit(9), geteBit(10), geteBit(11)]

gamma = (byte[11] * 1) + (byte[10] * 2) + (byte[9] * 4) + (byte[8] * 8) + (byte[7] * 16) + (byte[6] * 32) + (byte[5] * 64) + (byte[4] * 128) + (byte[3] * 256) + (byte[2] * 512) + (byte[1] * 1024) + (byte[0] * 2048)
epsilon = (ebyte[11] * 1) + (ebyte[10] * 2) + (ebyte[9] * 4) + (ebyte[8] * 8) + (ebyte[7] * 16) + (ebyte[6] * 32) + (ebyte[5] * 64) + (ebyte[4] * 128) + (ebyte[3] * 256) + (ebyte[2] * 512) + (ebyte[1] * 1024) + (ebyte[0] * 2048)

print(gamma * epsilon)
