with open('2015\Day 5\Input.in') as file:
    data = [i for i in file.read().strip().split("\n")]

string = ""

isNice = 0

vowels = 0
letters = 0
forbidden_strings = 0
lastChar = ""

for item in data:
    string = list(item)
    for char in string:
        if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
            vowels += 1
        if lastChar != "":
            if char == lastChar:
                letters += 1
            else:
                lastChar = char
        elif lastChar == "":
            lastChar = char
    if "ab" in item:
        forbidden_strings += 1
    if "cd" in item:
        forbidden_strings += 1
    if "pq" in item:
        forbidden_strings += 1
    if "xy" in item:
        forbidden_strings += 1
    print(item, ": ", vowels, " ", letters, " ", forbidden_strings, " ", lastChar)
    if vowels >= 3 and letters >= 1 and forbidden_strings == 0:
        print(item, ": ", vowels, " ", letters, " ", forbidden_strings, " ", lastChar)
        
        isNice += 1
    vowels = 0
    letters = 0
    forbidden_strings = 0

print(isNice)