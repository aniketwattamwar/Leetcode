s = "abc"
t = "ahbgdc"
p1 = 0
p2 = 0
for _ in range(len(t)):
    
    if s[p1] == t[p2]:
        p1+=1
        p2+=1
    else:
        p2+=1
    if p1 == len(s):
        print(True)

print(False)
