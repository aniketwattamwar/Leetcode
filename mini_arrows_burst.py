
points = [[10,16],[2,8],[1,6],[7,12]]
points.sort(key = lambda i:i[0])
output = [points[0]]
for start,end in points[1:]:
    prevEnd = output[-1][1]
    prevStart = output[-1][0]
    if start <= prevEnd:
        output[-1][0] = max(prevStart,start)
        output[-1][1] = min(prevEnd, end)
    else:
        output.append([start,end])
print(output)
print(len(output))



