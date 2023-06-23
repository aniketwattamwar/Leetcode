nums = [-1,0,1,2,-1,-4]
d = {}
for idx, num in enumerate(nums):
    d[num] = idx
triplet = []
ans = []
for i in range(len(nums)):
    for j in range(i,len(nums)):
        if i != j:
            two = nums[i] + nums[j]
            neg = -two
            if neg in d and d[neg] != i and d[neg]!=j:
                triplet = [nums[i],nums[j],neg]
                
                if sorted(triplet) not in ans:
                    ans.append(sorted(triplet))

# print(set(ans))
print(ans)