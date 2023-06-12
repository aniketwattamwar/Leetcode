## Good problem. Did not understand the problem
        ## Watch the techdose video for this problem
        ## Solve the hindex II problem as well.
        ## If to sort it in ascending, watch Timothy chang videos
citations = [3,0,6,1,5]
citations = sorted(citations)
for i, v in enumerate(citations):
    if len(citations) - i <= v:
        print(len(citations) - i)

print(0)