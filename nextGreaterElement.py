nums1 = [4,1,2]
nums2 = [1,3,4,2]


ans = []
for i in range(len(nums1)):
    for j in nums2:
        if nums1[i] == j:
            idx = nums2.index(j)
            if idx == len(nums2):
                ans.append(-1)
                break
            greater = nums2[idx+1]
            print(idx)
            if greater > j:
                ans.append(greater)
            else:
                ans.append(-1)

print(ans)

