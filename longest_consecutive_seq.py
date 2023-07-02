nums = [1,2,0,1,3]
nums = sorted(set(nums))
l = 0
r = l+1
print(len(nums))
mlen = 0
length = 0
lptr = l
while r < len(nums):

    if nums[l] == nums[r] - 1:
        
        length = len(nums[:r - lptr])
        l+=1
        r+=1
    else:
        l = r
        r = l+1
        lptr = l
    mlen = max(mlen,length)
print(mlen+1)