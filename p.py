print("enter the elements")
p=int(input())
for i in range(1,p+1):
   for j in range(p-i+1):
    print(end=" ")
   for k in range(i):
    print("*",end="") 
   for l in range(1,i):
    print("*",end="")
   print()	