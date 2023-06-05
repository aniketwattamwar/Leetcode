nums = [0,0,1,1,1,1,2,3,3]
pos = 0
for n in nums:
    if pos < 2 or n > nums[pos-2]:
        nums[pos] = n
        pos+=1




print(nums)
print(pos+1)