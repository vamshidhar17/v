a=int(input("enter first num to find gcd"))
b=int(input("enter the second num"))
c=[]
d=[]
for i in range(1,a+1):
    if a%i==0:
        c.append(i)
for j in range(1,b+1):
    if b%j==0:
        d.append(j)
for i in range(0,len(c)):
    for j in range(0,len(d)):
        if c[i]==d[j]:
            k=c[i]
print("the gcd of two nums is:"+str(k))
            
