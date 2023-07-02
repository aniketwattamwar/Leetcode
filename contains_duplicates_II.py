nums = [1,0,1,1]
k = 1
d = {}
for i in range(len(nums)):
    if nums[i] in d:
        diff = i - d[nums[i]]
        if diff <= k:
             
            print(True)
    else:
        d[nums[i]] = i

print(False)