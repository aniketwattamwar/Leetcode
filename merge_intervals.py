intervals = [[1,4],[5,6]]
 
ans = []
for i in range(1,len(intervals)):
    temp = []
    if intervals[i-1][1] >= intervals[i][0]:
        ith=intervals[i-1][0]
        jth = intervals[    i][1]
        ans.append([ith,jth])
        # ans.append([intervals[i][0],intervals[i+1][1]])
    else:
        ans.append(intervals[i])
print(ans)