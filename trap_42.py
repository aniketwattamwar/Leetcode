height = [4,2,0,3,2,5]
# height = [0,1,0,2,1,0,1,3,2,1,2,1]
all_trapped = 0
for i in range(1,len(height)-1):
    trapped = 0
    water_level= min(max(height[:i]),max(height[i:]))
    if water_level > 0 and trapped >= 0:
        trapped = water_level - height[i]
    if trapped > 0:
        all_trapped+=trapped
    
print(all_trapped)

