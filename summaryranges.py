nums = [0,1,2,4,5,7]

l = nums[0]
r = nums[0]
ans=[]
for i in range(1,len(nums)):

    if nums[i] ==r + 1:
        r=nums[i]
    else:
        if l!=r:
            ans.append(str(l) + "->" + str(r))
        else:
            ans.append(str(l))
        l = nums[i]
        r = nums[i]
if l!=r:
    ans.append(str(l) + "->" + str(r))
else:
    ans.append(str(l))
print(ans)