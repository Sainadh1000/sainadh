"""
CRM TASK 

CRM Task: Customer Discount Calculation
Objective: Create a Python program to calculate discounts for customers based on their type, partnership duration, and deal stage using variables, conditionals, operators, and a case match statement.
Task Requirements
Variables:
customerId 
customerName 
isPremium (boolean – true for premium customers)
yearsPartnership 
dealStage (String – "Proposal", "Negotiation", "Closed")
dealValue ( original value of the deal)
Conditional Statements:
Apply a base discount based on customer type and partnership years:
Premium customers: 10% discount.
Non-premium with ≥3 years partnership: 5% discount.
Others: 0% discount.
case match Statement:
Add an extra discount based on dealStage:
"Proposal": +2%
"Negotiation": +3%
"Closed": +5%
Calculation:
Calculate the final discount and discounted deal value.
Output:
Print customer details, base discount, extra discount, total discount, and final deal value.
"""
customerId=int(input("enter customerid: "))
customerName=input("enter cutomer name:")
isPremium=input("ispremium:")
yearsPartnership=int(input("years of patnership:"))
dealStage=input("enter deal stage:")
dealValue=int(input("enter deal value"))
discount=0.0
if isPremium=='yes':
    discount=0.10
elif isPremium=='no' and yearsPartnership>=3:
    discount=0.05
else:
    discount=0.0
match dealStage:
    case "proposal":
        discount+=0.02
    case "negotiation":
        discount+=0.03
    case "closed":
        discount+=0.05
discountvalue=dealValue*discount
finalprice=dealValue-discountvalue
print()
print(f"discount value is:{discountvalue}")
print(f"finalprice is:{finalprice}")