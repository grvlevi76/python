#<========== nested list ==========>
#manipulate specific nested list element through 2d array indexing exp x[1][2]
#check the size of list which has nested list and also check  size of nested list
#any other usage of eval() without using input()
#make a variable list with list() function and use input() and eval(input()) inside list()
#can  we make certain index of list a nested list by using  append
#what if u want to declare nested list at the out of range index of list

#last left -> creating nested list in range of index of list without eval(input()) combination

#enter 3 and 4 at 2nd index
x = [1,2]
#ans
x = [1,2,[]]     #first declare nested list
print("before any changes in list x : ",x)
x[2].append(3)
x[2].append(4)
print("\nwhole list x ->",x ,"with size",len(x))
print("nested list x[2] ->",x[2],"with size",len(x[2]))
#or 
x[2] = list(eval(input("enter nested list x[2] elements : ")))   #enter 3,4
print("list x -> ",x)

#experiment-> without declaring nested list inside list
#tuple nested list inside list
print("\nwithout declaring nested list inside list--->")
x[1]=eval(input("enter x[1] elements to make it nested list : ")) #whats this [1, (7, 8), [3, 4]]
print("list x = ",x)
print("nested list x[1] = ",x[1])



#observation ->
#the size of list x will not get affected even if u enter nested list inside of list