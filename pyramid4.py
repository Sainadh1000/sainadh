n=int(input("give no of iterations:"))
for i in range(n,0,-1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(1,2*i):
        print("*",end="")
    print()