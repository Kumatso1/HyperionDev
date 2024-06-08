# Create a list of menu items
menu = ["Coffee", "Tea", "Cake", "Sandwich"]

# Create a dictionary to store stock levels
stock = {
    "Coffee": 10,
    "Tea": 5,
    "Cake": 7,
    "Sandwich": 12
}

# Create a dictionary to store prices
price = {
    "Coffee": 2.50,
    "Tea": 1.80,
    "Cake": 3.00,
    "Sandwich": 4.00
}

# Calculate the total stock worth
total_stock_worth = 0
for item in menu:
  item_value = stock[item] * price[item]
  total_stock_worth += item_value

# Print the total stock worth
print(f"The total stock worth of the cafe is: ${total_stock_worth:.2f}")
