numbers = [1,2,7,11,15]
target = 9
d = {}
for idx, num in enumerate(numbers):
    d[num] = idx

print(d)
for i in range(len(numbers)):
    diff = 0
    diff = target - numbers[i]
    if diff in d:
        print([i,d[diff]])