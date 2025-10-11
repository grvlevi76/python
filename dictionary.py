#<======================== Dictionaries ==========================>

#dictionaries r type of data structure where data r stored in key-value pair within curly {} breacket
#same as hashmaping
#duplicate key r not allowed , if written then its value will overwrite previous one
#keys must be immutable like integer,string, tuple not list

math_marks = {1:25,2:26,3:27,4:22,5:21,6:"fail",'seven':23.3,4:20,6.6:0}
print(math_marks)
print("marks of roll no. 6 student : ",math_marks[6])
print("marks of roll no. 4 student : ",math_marks.get(4))
math_marks[1] = 10
print("marks of roll no. 1 student : ",math_marks[1])
math_marks[7] ="pass"
print(math_marks)

# to get the dictionaries value just write the key inside [ ] square breacket 
#different data type keys and values can exist within same dictionaries

#tuple as key in dictionaries------->>
math_marks[(9,8,7.7)] =[11,13,12]
print("dict after tuple as key :",math_marks)
print("tuple key :",math_marks[(9,8,7.7)])

math_marks[(7,8,9)] =6
print("dict after 2nd tuple as key :",math_marks)
print("2nd tuple key :",math_marks[(7,8,9)])

print("math_marks type :",type(math_marks))

#removing dictionary items------------->>>

print("\ndeleting -->")
#1 -> del -removes items by key
del math_marks[(9,8,7.7)]
print("after deleting through del:",math_marks)
#2 -> pop() -removes an element by key and returns its value
print("element deleted from dict through pop :",math_marks.pop((7,8,9)))
#3 -> popitem() -removes and returns the last key-value pair
key,val=math_marks.popitem()
print("deleted :",key,":",val)
print(math_marks)
#4 -> clear() - clears the dictionary

#<======================== nested dcitionary ==========================>
#top 3 student who got most marks
print("\nnested dictionary --->")
math_marks[(7,8,9)] = {7:29,8:28,9:30}
print("math_ marks dict :",math_marks)
print("nested dict : ",math_marks[(7,8,9)])
print("specific element in nested dict :",math_marks[(7,8,9)][9])

#iterate thorugh dictionary ----->>
#1 -> using key() - gets all keys
print("\nmath_marks dictionary keys :",)
for key in math_marks.keys():
    print(key)

#2 -> using values() - gets all values
print("math_marks dictionary values :")
for val in math_marks.values():
    print(val)

#3 -> using items() - gets all item
print("math_marks dict elements :")
for item in math_marks.items():
    print(item)