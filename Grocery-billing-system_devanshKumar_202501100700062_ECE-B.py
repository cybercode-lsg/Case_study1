# Grocery Store Billing System
# Author: YourName, RollNo, Section
# Department: Electronics & Communication Engineering

# Accept price and quantity for 5 items
prices = []
quantities = []

for i in range(5):
    price = float(input(f"Enter price of item {i+1}: "))
    quantity = int(input(f"Enter quantity of item {i+1}: "))
    prices.append(price)
    quantities.append(quantity)

# Calculate total cost
total_cost = sum([prices[i] * quantities[i] for i in range(5)])

# Apply discount if applicable
discount = 0
if total_cost > 100:
    discount = total_cost * 0.10

final_amount = total_cost - discount

# Display results
print("\n--- Billing Summary ---")
print(f"Original Total: Rs. {total_cost:.2f}")
print(f"Discount: Rs. {discount:.2f}")
print(f"Final Payable Amount: Rs. {final_amount:.2f}")