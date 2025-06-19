def main():
    print("Welcome to the Stock Portfolio Tracker!")

    # Hardcoded stock prices
    stock_prices = {
        "AAPL": 180,
        "TSLA": 250,
        "GOOGL": 140,
        "MSFT": 300,
        "AMZN": 130
    }

    portfolio = {}
    total_value = 0

    while True:
        stock = input("Enter stock symbol (or 'done' to finish): ").upper()
        if stock == 'DONE':
            break
        if stock not in stock_prices:
            print("Stock not found. Try again.")
            continue
        try:
            quantity = int(input(f"Enter quantity of {stock}: "))
            portfolio[stock] = quantity
        except ValueError:
            print("Invalid input. Please enter a number.")

    print("\nYour Portfolio:")
    for stock, quantity in portfolio.items():
        price = stock_prices[stock]
        value = price * quantity
        total_value += value
        print(f"{stock}: {quantity} shares @ ${price} each = ${value}")

    print(f"\nTotal Investment Value: ${total_value}")

    save = input("Do you want to save this to a file? (yes/no): ").lower()
    if save == 'yes':
        with open("portfolio_result.txt", "w") as file:
            for stock, quantity in portfolio.items():
                price = stock_prices[stock]
                value = price * quantity
                file.write(f"{stock}: {quantity} shares @ ${price} = ${value}\n")
            file.write(f"\nTotal Investment Value: ${total_value}\n")
        print("Portfolio saved to 'portfolio_result.txt'")

if __name__ == "__main__":
    main()
