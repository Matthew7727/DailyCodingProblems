stock_prices = [1, 3, 2, 8, 4, 1]
fee = 2 

def calculate_max_profit(prices, fee):
    hold = -prices[0] 
    cash = 0           

    for price in prices[1:]:
        hold = max(hold, cash - price)
        cash = max(cash, hold + price - fee)
    return cash

prices = [1, 3, 2, 8, 4, 10]
fee = 2
print(calculate_max_profit(prices, fee)) 
    