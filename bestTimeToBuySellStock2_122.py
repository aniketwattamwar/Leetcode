prices = [7,1,3,5,6,4]
# prices = [7,6,4,3,1]

## Current approach and logic is to implement
## the previous problem Buy and Sell stock I problem till every
## ith position. Basically, you find max profit twice before ith 
## and after ith and put that profit in an array

# minPrice = prices[0]
maxProfit = 0
# maxProfit2 = 0
# allProfits = []
# for j in range(len(prices)):
#     for i in range(j):
#         maxProfit = max(maxProfit, prices[i] - minPrice)
#         minPrice = min(minPrice, prices[i])
    
#     for i in range(j,len(prices)):
#         maxProfit2 = max(maxProfit2, prices[i] - minPrice)
#         minPrice = min(minPrice, prices[i])

#     allProfits.append(maxProfit + maxProfit2)


# print(max(allProfits))

## The solution is quite simple. I was overthinking and making it complex unnecessary.
for i in range(1,len(prices)):
    if prices[i] > prices[i -1]:
        maxProfit += prices[i] - prices[i-1]

print(maxProfit)


