item_price = float((input("Enter the price of the item: ")))
sales_tax_percentage = float(input("Enter the sales tax percentage: "))/100
total_price = round((item_price*sales_tax_percentage) + item_price,2)
print(f"Your total is ${total_price:.2f}")