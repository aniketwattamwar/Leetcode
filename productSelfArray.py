nums=[1,2,3,4]
ans  = [1]*len(nums)
pre = 1
post = 1
for i in range(len(nums)):
    ans[i]*=pre
    pre*=nums[i]
    ans[len(nums) - i - 1]*=post
    post *= nums[len(nums) - i -1]

print(ans)