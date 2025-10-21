# Write a Python program that counts how many vowels (a, e, i, o, u) are in a given sentence using a for

word=input("enter word:")
count=0
for i in word:
    if i.lower() in ['a','e','i','o','u']:
        count+=1
if count>0:
    print("no of vowels:",count)
else:
    print("no vowels")
