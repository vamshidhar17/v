def sorted(a):
   n=len(a)
   for i in range(n):
    for j in range(0,n-i-1):
       if a[j]>a[j+1]:
        [a[j],a[j+1]]=[a[j+1],a[j]]
   return a     

print("num of array elements")
q=int(input())		
print("enter list")
a=[]
for i in range(q):
   l=input()
   a.append(l)
sorted(a)
print("the sorted is",a)
		
