# ratings = [12,4,3,11,34,34,1,67]
ratings = [1,2,2]
left = [1]*len(ratings)
right = [1]*len(ratings)

for i in range(len(ratings)-1):
    if ratings[i] < ratings[i+1]:
        left[i+1]=left[i] + 1
# print(left)
for i in range(len(ratings) - 1,-1,-1):
    if i == 0:
        break
    if ratings[i] < ratings[i-1]:
        right[i-1]=right[i] + 1
# print(right)
ans = 0
for i in range(len(left)):
    ans+=max(left[i],right[i])

print(ans)