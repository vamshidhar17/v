print("enter the elements")
p=int(input())
for i in range(1,p+1):
   for j in range(2*(p+1)-1):
    print(end=" ")
   for k in range(1,i+1):
    print(k,end="  ") 
   for l in range(1,i):
    print(i-l,end="  ")
   print()	