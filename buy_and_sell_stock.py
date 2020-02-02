
# My solution
def buy_and_sell_stock_once(prices):
    i = 0
    j = 0
    start_day = 0
    end_day = 0
    maximum_profit = 0
    while i < len(prices) - 1:
        if prices[i] <= prices[i + 1]:
            if (prices[i + 1] - prices[j]) >= maximum_profit:
                maximum_profit = prices[i + 1] - prices[j]
                start_day = j
                end_day = i + 1
            i += 1
        else:
            i += 1
            if prices[j] >= prices[i] :
                j = i
    print(maximum_profit, start_day, end_day)
    # return maximum_profit

prices = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]

# prices = [110, 215, 180, 335, 5]
buy_and_sell_stock_once(prices)

# Time Complexity: O(n^2)
# Space Complexity: O(1)
def buy_and_sell_once(A):
  max_profit = 0
  for i in range(len(A)-1):
    for j in range(i+1, len(A)):
      if A[j] - A[i] > max_profit:
          max_profit = A[j] - A[i]
  return max_profit

print(buy_and_sell_once(prices))

# Time Complexity: O(n)
# Space Complexity: O(1)
def buy_and_sell_once(prices):
  max_profit = 0.0
  min_price = float('inf')
  for price in prices:
    min_price = min(min_price, price)
    compare_profit = price - min_price
    max_profit = max(max_profit, compare_profit)
  return max_profit

print(buy_and_sell_once(prices))