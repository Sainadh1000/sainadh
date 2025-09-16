n=int(input("give no of iterations:"))
for i in range(1,n+1):
    for j in range(1,n-i):
        print(" ",end="")
    for k in range(1,2*i):
        print("*",end="")
    print()