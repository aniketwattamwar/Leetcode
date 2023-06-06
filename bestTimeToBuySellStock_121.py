prices = [7,1,3,5,6,4]
# prices = [7,6,4,3,1]

## Brute force. solves 147/211 cases
# profit = 0
# m_profit = 0
# for i in range(len(prices)):
#     for j in range(i+1,len(prices)-1):
#         profit = prices[j] - prices[i]
#         if profit > m_profit:
#             m_profit = profit
# print(m_profit)

### Second approach
# profit = 0
# m_profit = 0
# length = len(prices)
# for i in range(len(prices)-1):
#     m = max(prices[i+1:length])
#     profit = m - prices[i]
#     if profit > m_profit:
#         m_profit = profit

# print(m_profit)
            
# Third approach. If you come across a minimum value keep on using that only.
minPrice = prices[0]
maxProfit = 0
for i in range(1,len(prices)):
    maxProfit = max(maxProfit, prices[i] - minPrice)
    minPrice = min(minPrice, prices[i])
    
print(maxProfit)

