data = open("2023\Day 1\Input.in").read().split('\n')
sum = 0
nums = []
fstnum = 0
lstnum = 0

for i in data:
    i = list(i)
    for j in i:
        if j.isnumeric():
            nums.append(j)
    fstnum = nums[0]
    lstnum = nums[len(nums)-1]
    nums.clear()
    sum += int(str(fstnum) + str(lstnum))
print(sum)