# Write a program in Python identifies the digit with the highest value and the digit with the lowest value within that number.

# Input:

# num1 = 9876543210
# num2 = -5082
# Output:


# Largest digit in 9876543210: 9
# Smallest digit in 987654321: 1

# Largest digit in -5082: 8
# Smallest digit in -5082: 0

num=int(input("enter number:"))
numlist=[]
while num>1:
    n=num%10
    numlist.append(n)
    num=num//10
print("maximum:",max(numlist))
print("minimun:",min(numlist))