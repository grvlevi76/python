#wrt a program to count no. of times letters appeared in string
str =(input("enter the string :"))
s = list(str)
n = len(s)
ltr = {}
for i in range(n):
    if s[i] not in ltr:
        ltr[s[i]] = 1
    else:
        val = ltr[str[i]]+1
        ltr[s[i]] = val

print("letters appeared vs times : ",ltr) 