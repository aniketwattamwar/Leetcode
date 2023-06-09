# nums = [2,3,1,1,4]
nums = [3,2,1,0,4]
n = len(nums)
last = nums[-1]
for i in range(len(nums)):
    if nums[i] == last - i - 1:
        print('True')
    
print("False")
