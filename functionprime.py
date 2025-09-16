divisible = [2, 3, 4, 5, 6, 7, 8, 9, 10]

def is_prime(num):
    if num < 2:
        print("Not prime")
        return
    for i in divisible:
        if i >= num:
            break  
        if num % i == 0:
            print("Not prime")
            return
    print("Is prime")

def main():
    num = int(input("Enter number: "))
    is_prime(num)

main()

