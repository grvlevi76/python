#<========================== list (linked list with array indexing lol) ====================>

#list basically stores sequences of individual haterogeneous object 
#preserves insertion order
#duplicate objects r allowed
#list is dynamic so we can increase or decrease size of it as we want  
print("lists -->")

#<----------declaration--------->>

print("\ndeclaration-->")
#no  need to declare size cause python doesn't compile whole code before execution
#we dont give size to list in python
x =[]  #list declaration(no need to give size)
y = [1,"yo",3]     #useful when total elements r sort and known
print("y list elements -> ",y)   #prints whole list -> [1,2,3]

#using list()
z = list(range(2,10,2))   #useful when total elements r long and known
print("z list elements : ",z)
s = 'ssup'
z = list(s)
print("z list elements : ",z)

#using split()
st = "ssup bud how r u"
q = s.split(st)
print("q list elements : ",q)

print("x, y and z list type : ",type(x),type(y),type(z))

#<------------insert in list----------->>

print("\ninsertion-->")
#1
x.append(1)      # inserts at end of the list
#2
y.insert(10, 5)   # Insert 5 at 10th index,  if entered index doesn't exist then it auto inserts at the end of list
print("list y elements : ",y)
print("y[3] = ",y[3])
#3
y[1] = 5         #replace value at specific index with another value
print("x and y list type : ",type(x),type(y))
#4
x = eval(input("enter list x elements : "))   #can take whole list elements as input from user in one go, just seperate each elements with comma
print("x list elments : ",x)
print("x and y list type : ",type(x),type(y))

#<------------ access elements in list ----------->

print("\naccess ->")

#1 - indexing
print("x[-1] and y[-1] : ",x[-1],y[-1])
#2 - slice [start:stop:step]
print("y[0::2] : ",y[0::2])
print("z[1::2]",z[1::2])

#<----------- traversal -------------------->

print("\ntraversal->")
#1 -for loop
for i in x:
    print(i)


#misc function of list------------->

print("\nother fuctions->")
#1 -len(y)
size = len(y) #4
print("y list size :",len(y))
#2 - z.count('s') - counts total 's' in list z
#3 - z.index('u') - tells the index of element 'u'
#4 - x.extend(y)
order1 = ["aloo","began"]
order2 = ["loki"]
order = order1.extend(order2)
print("extended order : ",order)
#5 - z.remove('p') - removes the element 'p'
#6 - z.pop(1) - removes the value at index 1

#learned today ->
#list creation through list(ranger(a,b,i)), funfact - tuple created through eval(input()) can get casted to list through list(eval(input()))
#types of lists , funfact - eval(input()) creates a tuple not list if no. of elements taken as input r more than 1 else type will be 'int'
