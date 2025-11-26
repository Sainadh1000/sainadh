# 2️ Longest Substring Without Repeating Characters

# Input: abcabcbb
# Output: abc (length = 3)
# No built-in shortcuts. Use pure logic.
word=input("Enter string: ")
longest=""
for i in range(len(word)):
    temp=""
    for j in range(i,len(word)):
        if word[j] not in temp:
             temp += word[j]
        else:
            break
    if len(temp)>len(longest):
        longest=temp
print("longest substring",longest)

# All Pairs With Given Sum
# List: [2, 4, 3, 5, 7, 8, 9]
# Sum = 7
# Output:
# (2,5)
# (4,3)

mylist = [2, 4, 3, 5, 7, 8, 9]
total = 7
for i in range(len(mylist)):
    for j in range(i + 1, len(mylist)): 
        if mylist[i] + mylist[j] == total:
            print((mylist[i], mylist[j]))

# Check if Two Strings Are Rotations

# Input:

# string1 = "ABCD"
# string2 = "CDAB"
string1=input("enter string1: ")
string2=input("enter string2: ")
if len(string1)==len(string2) and string2 in (string1+string1):
    print("two strings are rotation")
else:
    print("two strings are not rotations")


# 5 Compress the String
# Input: aaabbccccdaa
# Output: a3b2c4d1a2
originalstring = input("enter string: ")
compressedstring = ""
count=1
for i in range(1, len(originalstring)):
    if originalstring[i]==originalstring[i-1]:
        count+=1
    else:
        compressedstring+=originalstring[i-1]+str(count)
        count=1
compressedstring+=originalstring[-1]+str(count)
print(compressedstring)


            


    





        
    
        








 
    
