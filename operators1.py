a=110
b=98
#arithmatic operators
sum=a+b
sub=a-b
mul=a*b
div=a/b
mod=a%b
roundofdiv=a//b
exposquare=a**b
print(sum, sub, mul, div, mod, roundofdiv, exposquare)
a+=b
print(a)
b-=b
print(b)
a*=2
print(a)
#comparision operators
num1=12
num2=10
num3=20
num4=19
isequal=num1==num2
isnotequal=num1!=num2
print(isequal)
print(isnotequal)
isgreaterthanequal=num1>num2
print(isgreaterthanequal)
name1="sai"
name2="nadh"
print(name1==name2)
print(name1>name2)
#logical operators
d=num1>num2 and num3>num4
e=num1<num2 and num3<num4
g=f=num1<num2 or num3<num4
print(d)
print(e)
print(g)
#membership operators
str="i love python"
isapresent='a' in str
isppresent='p' in str
print(isapresent)
print(isppresent)
#identity operators
list1=[1,2,3]
list2=[1,2,3]
n1=10
n2=10
print(id(list1))
print(id(list2))
print(id(n1))
print(id(n2))
print(n1 is n2)
print(list1 is list2)
print(list1==list2)
#bitwise operators
n3=7
n4=9
r1=n3&n4
r2=n3|n4
r3=n3^n4
print(r1)
print(r2)
print(r3)
print(5>>4)
print(5<<4)
