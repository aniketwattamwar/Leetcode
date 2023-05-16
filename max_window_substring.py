s = "ADOBECODEBANC"
t = "ABC"

# s = "cabwefgewcwaefgcf"
# t = "cae"  

subs = "ADOBECODEBANC"
ans = ""
# for i in range(len(s)):
#     l = len(t)
#     substring = ""
#     for let in s[i:]:
#         if l > 0: 
#             substring+=let
#         if let in t:         
#             l-=1
#         if l == 0:
#             break
#     print(substring)
#     if len(subs) >= len(substring) and len(substring) >= len(t) and l == 0:
#         ans = substring
   
# print(ans)
import collections
from collections import defaultdict
t_map = collections.Counter(t)
subs=[]
for i in range(len(s)):
    
    substring = ""
    ans =""
    s_map = collections.Counter(defaultdict(int))
    for let in s[i:]:
        ans+=let
        if let in t_map: 
            s_map[let]+=1

            if s_map == t_map:
                substring+=ans
                break
    subs.append(substring)

sub = list(set(subs))
sub = sub[1:]
s = sorted(sub,key=len)
ss = s[0:1]
ss = "".join(ss)

print(ss)

