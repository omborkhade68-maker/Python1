# Stock Portfolio Tracker

stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "AMZN": 170,
    "MSFT": 400
}

stock_name = input("Enter stock name: ").upper()
quantity = int(input("Enter quantity: "))

if stock_name in stocks:
    price = stocks[stock_name]
    total = price * quantity

    print("\nStock:", stock_name)
    print("Price: $", price)
    print("Quantity:", quantity)
    print("Total Investment: $", total)

    # Optional: save result
    with open("portfolio.txt", "w") as file:
        file.write("Stock: " + stock_name + "\n")
        file.write("Quantity: " + str(quantity) + "\n")
        file.write("Total Investment: $" + str(total))

    print("Result saved in portfolio.txt")

else:
    print("Stock not available!")



