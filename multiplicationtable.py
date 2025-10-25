# Print Full Multiplication Table
# The multiplication table from 1 to 10 is a table that shows the products of numbers from 1 to 10.

# Write a code to generates a complete multiplication table for numbers 1 through 10.

# Given:

# multiplication table of: 1
#  1 2 3 4 5 6 7 8 9 10
# multiplication table of: 2
#  2 4 6 8 10 12 14 16 18 20

for i in range(1,11):
    print("multiplication table of :",i)
    for j in range(1,11):
        print(f" {i*j}" ,end="")
    print()