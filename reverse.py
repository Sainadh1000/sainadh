# Goal:
# Write a Python program that takes a number from the user and prints its reverse using a while loop.

# 🧩 Instructions:

# Ask the user to enter a number (integer).

# Use a while loop to extract digits one by one using modulus (%) and integer division (//).

# Build the reversed number.

# Print the reversed number at the end.

n=int(input("enter number:"))
reverse=0
while n>0:
    digit=n%10
    reverse=reverse*10+digit
    n=n//10
print("reversenumber:",reverse)
