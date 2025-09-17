mylist=[10,29,34,42,76,21,0,21,10]
mylist.append(54)
print(mylist)
mylist.append([1,2])
print(mylist)
mylist.extend([3,4,5])
print(mylist)
mylist.insert(2,4)
print(mylist)
mylist.pop()
print(mylist)
mylist.pop(1)
print(mylist)
#mylist.remove(0) use to remove the 0 element for the list not element in 0 index
#print(mylist)
mylist.clear()
print(mylist)
newlist=[10,2,5,7,8,4,1]
a=newlist.index(10)
print(a)
b=newlist.index(1,3)
print(b)
c=newlist.index(5,2,4)
print(c)
newlist.extend([10,10,10])
print(newlist.count(10))
list_nums = [10,20, 30,40,50]
print(list_nums)
list_nums.reverse()
print(list_nums)

newlist.sort(reverse=False)#ascending order
print(newlist)
newlist.sort(reverse=True)#descending order
print(newlist)

#soft copy
copiedlist=newlist
newlist.append(100)#if newlist is updated copiedlist also updated
print(copiedlist)
print(newlist)