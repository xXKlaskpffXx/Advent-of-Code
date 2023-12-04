data = open('2023\Day 4\Input.in').read().split('\n')
winnings = []
nums = []

wins = 0
sum = 0

card_wins = []
card_wins2 = []

def vacuum(a):
    b = []
    for i in a:
        if not i == '':
            b.append(i)
    return b

for i in data:
    i = i.split(': ')[1]
    w = i.split(' | ')[0]
    n = i.split(' | ')[1]
    for j in w.split(' '):
        winnings.append(j)
    for j in n.split(' '):
        nums.append(j)
    
    winnings = vacuum(winnings)
    nums = vacuum(nums)

    for k in nums:
        if k in winnings:
            wins += 1
    card_wins.append(wins)
    nums.clear()
    winnings.clear()
    wins = 0
#print(card_wins)

for i in range(len(card_wins)):
    card_wins2.append(1)

for i in range(len(card_wins)):
    for j in range(card_wins[i]):
        card_wins2[j+i+1] += card_wins2[i]
    

for i in card_wins2:
    sum += i
print(sum)