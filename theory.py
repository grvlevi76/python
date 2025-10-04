#<-------- dynamic data type --------->

#no  need to specify data type
n =6; #declared variable

#<=============== taking input ==================>

#caste the input in whatever data type of value u want from user
n = int(input("enter the number : "))  

#<========================== list (dynamic array) ====================>

#no  need to declare size cause python doesn't compile whole code before execution
#we dont give size to list in python
x =[]  #list declaration(no need to give size)
y = [1,2,3]  

print("y list elements -> ",y)   #prints whole list -> [1,2,3]
#wrong --will throw error ->
#print(x[0])           #❌there's no size of x right now so there's no element in it unlike c's default 0 value
#x[1] = int(input())   # ❌again error cause x list with 1 index doesn't exit to store user input unlike c default compiled time allocation

#insert in list
x.append(1)      #to insert at end of the list
y.insert(1, 4)   # Insert 4 at 1th index
y[1] = 5         #replace value at specific index with another value

#lenth of list
size = len(y) #4
print("y list size :",len(y))

#<========================= conditional statement ========================>

#<========================= loops ========================>

#for-else loop ===>
#in python A 'for' loop is iterator-based, not condition-checking like in C.
#range(0, n+1) generates the sequence [0,1,2,3,...,n]
#Python internally pulls the next element from that sequence.
#When no more elements exist, the loop exits.

for i in range(size):       #range decodes 'size' to 0,1,2,3 and then 'i' will run with each decoded value for loop's iteration(i =0,i=1,i=2....) 
    print("inside loop i = ",i)
    if i ==3:
        print("loop break without completing last iteration")
        break
else:                        # 'else' just after 'for loop' is used to check  if loop has completed all its iteration or not
    print("loop completed all its iteration")

print("outside loop i = ",i)


#<-------------questions-------->
#how loops knows their scope when their's no curly breacket? how does it uses tab to recognise its scope
#hint - loops,if-else they do not create scope