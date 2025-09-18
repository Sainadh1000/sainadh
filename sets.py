# empty sets
empty_set = {} # always a dict
print(type(empty_set))

# using class
empty_set = set()
print(type(empty_set))

set_nums = {10,20,30,40,50,10,20}
print(set_nums) # Unordered, Unique {50, 20, 40, 10, 30} no repeted values
#print(set_nums[1])# indexing not posible for sets

set_nums.add(70)
print(set_nums)
#set_nums.add(80,90) add allows one argument
set_nums.add("sai")
print(set_nums)

#set_nums.update(34) only allows itreble objects
set_nums.update([1,"sai"])# since sai is already exist only 1 gets updated
print(set_nums)
set_nums.update({56,76,"dinesh"})
print(set_nums)

set_nums.discard("sai")
print(set_nums)
# set_nums.remove(100) # KeyError: 100
print(set_nums)

# discard() -> removes a specific element, if element is not found
# no error
print(set_nums)
set_nums.discard(100) # No KeyError: 100
print(set_nums)

# pop() -> removes random element and returns the element removed
removed_element = set_nums.pop()
print(set_nums)
print(removed_element)
set_nums.add(removed_element)
print(set_nums)

set_nums.clear()
print(set_nums)

s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}
s3 = s1.union(s2)#returns a new sets, with all the unique elements
print(s1.union(s2)) 
print(s3)
s4 = s1 | s2# | represent union
print(s4)

s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}
s3 = s1.intersection(s2)# returns a new sets, with all the common elements
print(s1.intersection(s2))
print(s3)
s4 = s1 & s2#& represent intersection
print(s4)

# intersection_update() -> updates the calling set to keep only the items found in both sets(common) 
# modifies the original set -> doesn't return a set again
s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}
print(s1.intersection_update(s2))#returns none since it updates the to the calling set
print(s1)
print(s2)

# difference() -> returns a new set with elements consisting only the elements in first set not the second
# you can also use symbol -
s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}
print(s1.difference(s2)) # prints {10,20,30} since 40 and 50 are in second set s2
print(s2.difference(s1))#prints {60,70,80} since 40 and 50 are in second set S1
print(s1)
print(s2)


# difference_update() -> update the original set calling, returns nothing
s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}
print(s1.difference_update(s2))
print(s1)
print(s2)

# symmetric_difference() -> returns a set, with elements that are 
# either of the sets, but not both (exclude common elements)
# you can also use symbol ^
s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}
print(s1.symmetric_difference(s2))
print(s1 ^ s2)
print(s1)
print(s2)

# symmetric_difference_update() -> update the original set calling, 
#  with elements that are either of the sets, but not both 
# (exclude common elements)
s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}
print(s1.symmetric_difference_update(s2))
print(s1)
print(s2)

# issubset() -> checks whether all elements of one set are present
# in another set
s1 = {10,20,30,40,50}
s2 = {30,40,50}
s3 = {30,40,50,60}
print(s2.issubset(s1)) # all elemnets are present so returns true
print(s3.issubset(s1)) # 60 is not present in s1 so returns false

# issuperset() -> checks whether a set contains 
# all the elements of another set
s1 = {10,20,30,40,50}
s2 = {30,40,50}
print(s1.issuperset(s2))# true s1 has all the elements of s2
print(s2.issuperset(s1))# false 60 is not present in s1

# isdisjoint() -> checks if two sets have no common elements
s1 = {10,20,30,40,50}
s2 = {30,40,50}
s3 = {60,70,80}
print(s1.isdisjoint(s2))
print(s1.isdisjoint(s3))

# Frozenset
s1 = {10,20,30,40,50}
s1.add(60)
print(s1)

fs1 = frozenset({10,20,30,40,50})
print(type(fs1))
#fs1.add(60) forzenset doesn'tcontain add method we are able to update data we can only access the dataS
print(dir(fs1))
print(fs1)