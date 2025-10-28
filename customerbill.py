# Task 2: Customer Shopping Bill Calculator

# Description:
# Simulate a shopping experience where a customer adds multiple products and gets a final bill.

# Requirements:

# Ask for Customer ID and Name.

# Continuously ask for Product Name, Price, and Quantity.

# Allow user to add multiple products until they type “No”.

# Compute total cost, GST (18%), and final amount.

# Print a bill summary showing each product and totals


cid=int(input("enter customerid:"))
name=input("enter name")
products=[]
totalcost=0
gst=18
while True:
    product=input("enter product:")
    price=int(input("enter price:"))
    quantity=int(input("enter quantity:"))
    addproducts=input("do you want to add more products(yes/no):")
    totalcost+=price*quantity
    products.append(product)
    if addproducts.lower()!='yes':
        break
gst_amount = (totalcost * gst) / 100
finalprice = totalcost + gst_amount
print("-----------bill---------------")
print(f"products purchased{products}")
print(f"totalprice:{totalcost}")
print(f"gst:{gst}")
print(f"total amount:{finalprice}")
    