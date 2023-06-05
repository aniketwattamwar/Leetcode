nums = [0,0,1,1,1,1,2,3,3]
pos = 0
for i in range(1,len(nums)):
    if nums[pos] != nums[i]:
        pos+=1
        nums[pos] = nums[i]
print(nums)
print(pos+1)