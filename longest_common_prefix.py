strs = ["flower","flow","flight"]

if len(strs) == 0:
    print("")
    
base = strs[0]
for i in range(len(base)):
    for word in strs[1:]:
        if word[i]!= base[i] or i == len(word):
            print(base[0:i])

            