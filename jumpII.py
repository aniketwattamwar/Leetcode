nums=[1,2,1,1,1]
# nums =[2,2,3]
# steps =1
# idx = 1
# for i in range(len(nums)):
#     if nums[i] == len(nums) - 1 - i:
#         print(steps)
#     if idx < 0:
#         print(steps)
#     idx = max(idx,nums[i])
#     idx-=1
#     steps+=1

# print(steps)

steps = 0
mx = 0
curr = 0
for i in range(len(nums)):

    mx = max(mx,i+nums[i])
    if i == curr:
        steps+=1
        curr = mx
    if curr >= len(nums)-1:
        print(steps)
    if i>= mx:
        print(0)
print(steps)