data = open('2023\Day 4\Input.in').read().split('\n')
winnings = []
nums = []

product = 0
sum = 0

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
            if product == 0: product = 1
            else: product *= 2
    nums.clear()
    winnings.clear()
    sum += product
    product = 0
print(sum)