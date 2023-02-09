words = ["abc","deq","mee","aqq","dkd","ccc"]
pattern = "abb"
ans = []
for word in words:
    maper = {}
    mapper1 = {}
    flag = 0
    for l,m in zip(word,pattern):
        if maper.get(m,l)==l and mapper1.get(l,m)==m:
            maper[m] = l
            mapper1[l] = m
        else:
            flag = 1
            break
    if not flag:
        ans.append(word)
print(ans)