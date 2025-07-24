stock_prices={
    "AAPL": {"price": 180, "name": "Apple"},
    "TSLA": {"price": 250, "name": "Tesla"},
    "MSFT": {"price": 340, "name": "Microsoft"},
    "AMZN": {"price": 125, "name": "Amazon"},
    "GOOGL": {"price": 135, "name": "Google"},
    "META": {"price": 290, "name": "Meta"},
    "NFLX": {"price": 450, "name": "Netflix"},
    "NVDA": {"price": 750, "name": "Nvidia"},
    "JPM": {"price": 155, "name": "JP Morgan Chase"},
    "DIS": {"price": 90, "name": "Disney"},
}

stock = input("Enter the code of the stock you invested in:").upper()
if stock in stock_prices:
    shares= int(input("Enter the number of shares you own :"))
    total = stock_prices[stock]["price"]* shares
    print(f"The total amount you invested in {stock_prices[stock]["name"]} is ${total}")
    with open ("stocks.txt",'w+') as file:
        file.write(f'Test run: It is working\n')
        file.write(f"Stock: {stock} ({stock_prices[stock]['name']})\n")
        file.write(f"Number of shares: {shares}\n")
        file.write(f"Total investment: ${total}\n")
        
    print("Investment details saved to 'stocks.txt'.")
else:
    print("Stock info not listed in the database.")
    
