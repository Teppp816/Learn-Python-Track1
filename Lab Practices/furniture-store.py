# Receipts for Lovely Loveseats

# In this project, we will be storing the names and prices of a furniture store’s catalog in variables. You will then process the total price and item list of customers, printing them to the output terminal.

lovely_loveseat_description = """Lovely Loveseat. Tufted polyester blen on wood.
32 inches high x 40 inches deep.
Red or white."""

lovely_loveseat_price = 254.00

stylish_settee_description = """ Stylish Sette. Daux leather on birch.
29.50 inches high x 54.75 inches wide x 28 inches deep.
Balck."""

stylish_settee_price = 180.50

luxurius_lamp_description = """Luxurious Lamp. Glass and iron. 
36 inches tall. 
Brown with cream shade."""

luxurious_lamp_price = 52.15

sales_tax = .088

customer_one_total = 0
customer_one_itemization = ""

customer_one_total += lovely_loveseat_price
customer_one_itemization += lovely_loveseat_description

customer_one_total += luxurious_lamp_price
customer_one_itemization += luxurius_lamp_description

customer_one_tax = customer_one_total * sales_tax
customer_one_total += customer_one_tax

print("Customer One Items: ")
print(customer_one_itemization)

print("Customer One Total: ")
print(customer_one_total)

# Congratulations! We created our catalog and served our first customer. We used our knowledge of strings and numbers to create and update variables. 
# We were able to print out an itemized list and a total cost for our customer