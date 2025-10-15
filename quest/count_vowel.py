#count no. of times vowel appeared in string 
word = input("enter the string : ")
vw= ('a','e','i','o','u')
let = {}
for i in word:
    if i in vw:
        let[i] = let.get(i,0)+1

for key,val in let.items():
    print(key,"appeared",val,"times")