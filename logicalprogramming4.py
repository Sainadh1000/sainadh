# Remove Duplicates Without set()
# From a list [1,2,2,3,4,4] → [1,2,3,4]
mylist=[1,2,2,3,4,4]
myuniquelist=[]
for i in mylist:
    if i not in myuniquelist:
        myuniquelist.append(i)
print(myuniquelist) 

# Second Largest Number
# Find the second largest number in a list without sorting.
largelist=[1,32,33,6,8]
newlist=[]
maxvalue=max(largelist)
for i in largelist:
    if i==maxvalue:
        continue
    else:
        newlist.append(i)
secondmaxvalue=max(newlist)
print(secondmaxvalue)


# Word Frequency Counter
# Count how many times each word appears in a sentence.
sentence="hello welcome to python here we learn python and django hello"
words=sentence.split()
countdict={}
for i in words:
    if i in countdict:
        countdict[i]+=1
    else:
        countdict[i]=1
print(countdict)

#First Non-Repeating Character
mystring=input("enter string:")
strlist=[]
for i in mystring:
    if i not in strlist:
        if mystring.count(i)==1:
            strlist.append(i)
if strlist:
    print(strlist[0])
else:
    print("No non-repeating character")

    


