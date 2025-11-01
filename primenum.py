num = int(input("Enter number: "))

if num <= 1:
    print("Not prime")
else:
    for i in range(2, num):
        if num % i == 0:
            print("Not prime")
            break
    else: #else after a loop (for or while) means:“Run this code only if the loop didn’t end by a break.”
        print("Prime")




mylist=[1,5,8,9,4]
primelist=[]
for i in mylist:
    if i<=1:
        continue
    else:
        for j in range(2,i):
            if i%j==0:
                break
        else: #else after a loop (for or while) means:“Run this code only if the loop didn’t end by a break.”
            primelist.append(i)
print(primelist)
