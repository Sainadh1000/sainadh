
# Palindrome Checker
# Input a string and check if it reads the same forwards and backwards.

a=input('enter word:')
if a == a[::-1]:
    print(f"{a} is palindrome")
else:
    print("not palindrome")



# Find Factorial of a number

num = int(input("Enter number: "))

if num < 0:
    print("Factorial is not defined for negative numbers")
else:
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    print(f"Factorial of {num} is {factorial}")




# Check Prime or Not

pnum=int(input("enter number: "))
if pnum<=1:
    print("not prime")
else:
    for i in range(2,pnum):
        if pnum%i==0:
            print("not a prime")
            break
    else:
        print("prime")


# Reverse a string without built-in functions
rs = input("Enter word: ")
reversed_str = ""
for i in rs:
    reversed_str = i + reversed_str
print(reversed_str)




# Count vowels and consonants in a string
vs=input("enter string: ")
vcount=0
ccount=0
for i in vs:
    if i=='a' or i=='e' or i=='i' or i=='o'  or i=='u':
        vcount +=1
    else:
        ccount +=1

print(f"vowels count {vcount}")
print(f"consonants count {ccount}")   





