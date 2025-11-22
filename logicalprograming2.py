# Find largest of 3 numbers
a = int(input("Enter number a: "))
b = int(input("Enter number b: "))
c = int(input("Enter number c: "))

if a>=b and a>=c:
    maxnumber = a
elif b>=a and b>=c:
    maxnumber=b
else:
    maxnumber=c
print(f"Largest number is:{maxnumber}")


# Sum of digits of a number
# Example: 123 → 1+2+3 = 6
snum=int(input("enter number:"))
sum=0
while snum>0:
    div=snum%10
    sum+=div
    snum=snum//10
print(sum)


# Print Fibonacci series up to N terms
n = int(input("Enter number of terms: "))

a, b = 0, 1

print("Fibonacci Series:")
for i in range(n):
    print(a ,end=" ")
    a,b=b,a+b



print()


# Swap two numbers without third variable
n1=int(input("enter n1: "))
n2=int(input("enter n2: "))
n1,n2=n2,n1
print(n1)
print(n2)



# Check if a number is Armstrong number
anum=int(input("enter number: "))
sum=0
temp=anum
s=str(anum)
p=len(s)
for i in range(p):
    div=anum%10
    sum+=div**p
    anum //=10
if temp==sum:
    print("is armstrong")
else:
    print(" is not armstrong")
