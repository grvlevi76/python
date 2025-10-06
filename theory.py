#<-------- dynamic data type --------->

#no  need to specify data type
n =6; #declared variable

#<=============== taking input ==================>

#caste the input in whatever data type of value u want from user
n = int(input("enter the number n : "))        #takes only one value as a input from user at a time
m = eval(input("enter the m list elements : "))  #we can take all elements of list as input from user
print("m list elements : ",m)
print("n and m  list type : ",type(n),type(m))


#<======================== tuple ==========================>
#tuple is sequences of homogenous objects 
#or in lame language tuple is collection of same data type value
#weird but haterogenous elements taken as input through eval(input()) makes list a tuple

#<========================= conditional statement ========================>

#<========================= loops ========================>

print("\nloops--->")
#for-else loop ===>
#in python A 'for' loop is iterator-based, not condition-checking like in C.
#range(0, n+1) generates the sequence [0,1,2,3,...,n]
#Python internally pulls the next element from that sequence.
#When no more elements exist, the loop exits.

for i in range(4):       #range decodes '4' to 0,1,2,3 and then 'i' will run with each decoded value for loop's iteration(i =0,i=1,i=2....) 
    print("inside loop i = ",i)
    if i ==3:
        print("loop break without completing last iteration")
        break
else:                        # 'else' just after 'for loop' is used to check  if loop has completed all its iteration or not
    print("loop completed all its iteration")

print("outside loop i = ",i)


#<-------------questions-------->
#eval(input()) converts the variable or list into 'tuple' if multiple elements r taken as input
# how loops knows their scope when their's no curly breacket? how does it uses tab to recognise its scope
#hint - loops,if-else they do not create scope