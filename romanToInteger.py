d = {'I': 1, 'V': 5, 'X': 10, 'L':50, 'C':100, 'D':500, 'M':1000}
s = "MCMXCIV"
ans = 0
rem = 1
# for val in s:
#     temp = 1
#     if val in d:
#         temp = d[val]
#         ans= ans+temp 
# print(ans)

for i in range(len(s) - 1):
    if d[s[i]] < d[s[i+1]]:
        ans-=d[s[i]]
    else:
        ans+=d[s[i]]
print(ans+d[s[-1]])
