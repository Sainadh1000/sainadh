def fibonacci(n):
    fibonacciseries = []
    a = 0
    b = 1
    for _ in range(n):
        fibonacciseries.append(a)
        a,b=b,a+b 
    return fibonacciseries
print(fibonacci(10))

def calculator(a,b,o):
    if o=='add':
        print(a+b)
    elif o=='sub':
        print(a-b)
    elif o=='div':
        print(a/b)
    elif o=='mul':
        print(a*b)
    else:
        print(a%b)
calculator(12,10,'add')

def listduplicator(lst):
    seen = set()
    unique_list = []
    for item in lst:
        if item not in seen:
            unique_list.append(item)
            seen.add(item)
    return unique_list

my_list = [1, 2, 2, 3, 4, 3, 5, 1, 6]
print(listduplicator(my_list))