mydictionary={"a":"apple","b":"banana"}
print(mydictionary["a"])
#print(mydictionary[0]) indexing is not posible for dictionaries

mydictionary.update({"c":"cherry"})
print(mydictionary)
mydictionary.update({"a":"apricot","d":"dragon fruit"})
print(mydictionary)

#mydictionary.pop() in dictionaries pop expect atleast one argument
mydictionary.pop("a")
print(mydictionary)

mydictionary.popitem()# remove last inserted item no arguments required
print(mydictionary)

mydictionary.clear()
print(mydictionary)

dict_courses = {"course1":"python","course2":"java","course3":"cloud"}
print(dict_courses["course2"])
# print(dict_courses["course4"]) # KeyError: 'course4'

# get() -> Access the value using key, if key not found no error
print(dict_courses.get("course2"))
print(dict_courses.get("course4","Upcoming Course"))

print(dict_courses.keys())#dict_keys(['course1', 'course2', 'course3'])
print(dict_courses.values())#dict_values(['python', 'java', 'cloud'])
print(dict_courses.items())#dict_items([('course1', 'python'), ('course2', 'java'), ('course3', 'cloud')])

dict_courses = {"course1":"python","course2":"java","course3":"cloud"}

dict_courses_copy = dict_courses.copy()
print(dict_courses_copy)

dict_courses_copy["course3"] = "devops"
print(dict_courses_copy) # only duplicate dictionary gets updated original remains same
print(dict_courses)

dict_courses = {"course1":"python","course2":"java","course3":"cloud"}
dict_courses_copy_soft = dict_courses
dict_courses_copy_soft["course3"] = "devops"
print(dict_courses_copy_soft)# both dictionaries updated
print(dict_courses)

value = dict_courses.setdefault("course4","devops")
print(value)
print(dict_courses)# since course4 is not there its get updated by default value

value2 = dict_courses.setdefault("course4","django")#key is present so not updated
print(value2)
print(dict_courses)