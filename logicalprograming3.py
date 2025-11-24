# Check if a number is Perfect Number (e.g., 6 → 1+2+3 = 6)
pnum=int(input("enter number:"))
total=0
for i in range(1,pnum):
    if pnum%i==0:
        total+=i
if total==pnum:
    print("perfect number")
else:
    print("not perfect number")


# Check if a number is Strong Number (145 → 1! + 4! + 5! = 145)
snum=int(input("enter number: "))
csnum=snum
factsum=0
while csnum>0:
    div=csnum%10
    fact=1
    for j in range(1,div+1):
        fact *=j
    factsum +=fact
    csnum=csnum//10
if snum==factsum:
    print("strong number")
else:
    print("not a strong number")




# Find LCM and GCD of two numbers
a=int(input("enter number: "))
b=int(input("enter number: "))
adivisor=set()
bdivisor=set()
for i in range(1,a+1):
    if a%i==0:
        adivisor.add(i)
for j in range(1,b+1):
    if b%j==0:
        bdivisor.add(j)
common_divisor = adivisor.intersection(bdivisor)
gcd=max(common_divisor)
lcm=a*b/gcd
print(f"lcm of {a},{b} is {lcm}")
print(f"gcd of {a},{b} is {gcd}")

    


# Check if a number is Harshad (Niven) Number
a=int(input("enter number: "))
acopy=a
total=0
while acopy>0:
    div=acopy%10
    total +=div
    acopy=acopy//10
if a%total==0:
    print(f"{a} is Harshad Niven number")
else:
    print(f"{a} is not Harshad niven number")



# Convert Decimal to Binary / Octal / Hexadecimal
dnum=int(input("enter number: "))
def convert(num,a):
    digits = "0123456789ABCDEF"
    result=''
    if num==0:
        return "0"
    while num>0:
        div=num%a
        result=digits[div]+result
        num=int(num/a)
    return result
binaryconvert=convert(dnum,2)
octalconvert=convert(dnum,8)
hexadecimalconvert=convert(dnum,16)
print(f"hexadecimal: {hexadecimalconvert}")
print(f"binary: {binaryconvert}")
print(f"octal: {octalconvert}")
   
         


# Find Sum of even and odd digits separately
num=int(input("enter number:"))

evensum=0
oddsum=0
while num>0:
    div=num%10
    if div%2==0:
        evensum +=div
    else:
        oddsum +=div
    num=num//10
print(evensum)
print(oddsum)

# Check if a number is Spy Number (sum of digits = product of digits)
spnum=int(input("enter number: "))
spnumcopy=spnum
total=0
product=1
while spnumcopy>0:
    div=spnumcopy%10
    total +=div
    product *=div
    spnumcopy=spnumcopy//10
if product==total:
    print(f"{snum} is SPY number")
else:
    print(f"{snum} is not SPY number")


# Find all Prime numbers in a given range
pn1=int(input("enter value1: "))
pn2=int(input("enter value2: "))
primelist=[]
if pn1>pn2:
    pn1,pn2=pn2,pn1
for i in range(pn1,pn2):
    if i < 2:
        continue
    for j in range(2,i):
        if i%j==0:
            break
    else:
        primelist.append(i)
print(primelist)

      
    

    