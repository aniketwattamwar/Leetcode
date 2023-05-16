s = "AABABBA"
k = 1

def characterReplacement(s, k):

    d={}
    l=0
    output = 0
    for i in range(len(s)):
        if not s[i] in d:
            d[s[i]]=0
        d[s[i]] += 1
        window = i - l + 1
        
        if window - max(d.values()) <=k:
            output = max(output,window)
        else:
            d[s[l]]-=1
            if not d[s[l]]:
                d.pop(s[l])
            l+=1

    return output

out = characterReplacement(s,k)
print(out)