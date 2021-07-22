#find maximum profit of the stock prices

stock_prices=[23,44,53,11,2,3,178,98]

#21+9+1+175


profit=0
for i in range(1,len(stock_prices)):
    if stock_prices[i]>stock_prices[i-1]:
        profit+=stock_prices[i]-stock_prices[i-1]

print(profit)
