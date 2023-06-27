# nums = 
# nums = [12,28,83,4,25,26,25,2,25,25,25,12]
nums = [5,1,3,5,10,7,4,9,2,8]
target = 15
if sum(nums) < target:
    print(0)
# nums.sort()
l = 0 
n = len(nums)
r = n - 1
length = n
mini_len = n
pre = [nums[0]]*(n)
for i in range(1,n):
    pre[i]= pre[i-1]+ nums[i]
print(pre)
while l < r:
    diff = pre[r] - pre[l]
    if diff >= target:
        length = r - l 
        l+=1
    else:
        break
    if length < mini_len:
        mini_len = length

print(mini_len)

# l = 0
# r = 0
# s=0
# ans = []
# length = float('inf')
# while r < len(nums):
#     s+=nums[r]
#     if s >= target:
#         while(s>=target):
#             s-=nums[l]
#             l+=1
#         length = min(length,r-l+2)
#     r+=1
# print(length)
# if length == float('inf'):
#     print(0)
# else:
#     print(length)
