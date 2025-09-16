def is_prime():
    num = int(input("Enter number: "))
    if num < 2:
        print("Not prime")
        return
    for i in range(2, num):
        if num % i == 0:
            print("Not prime")
            return
    print("Prime")
is_prime()