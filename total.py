# Find the Sum of All Even Numbers
# Ask the user to enter a number (say n).

# Use a for loop to go through all numbers from 1 to n.

# Check if the number is even (number % 2 == 0).

# Add all even numbers together.

# Print the final sum.

n=int(input("enter number:"))
sum=0
for i in range(n+1):
    if i%2==0:
        sum+=i
if sum>0:
    print("total sum of even numbers is:",sum)
else:
    print("no even numbers")