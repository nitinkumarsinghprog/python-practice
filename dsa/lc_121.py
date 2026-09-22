def max_profit(prices):
    min_value = prices[0]
    max_value = 0

    for i in range(1, len(prices)):
        if prices[i] < min_value:
            min_value = prices[i]
        profit = prices[i] - min_value
        if profit > max_value:
            max_value = profit

    return max_value

print(max_profit([7,1,5,3,6,4])) 