temps_c = [0, 20, 37, 100]
temps_f=list(map(lambda x: (9/5)*x+32,temps_c))
print(temps_f)

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
oddnums=list(filter(lambda x:x%2!=0,nums))
print(oddnums)

words = ["apple", "banana", "cherry", "blueberry", "kiwi"]
from functools import reduce
longestword=reduce(lambda x,y: x if len(x)>len(y)  else y ,words)
print(longestword)