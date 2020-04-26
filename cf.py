n=int(input())
p=0
b=[]
q=0
for i in range(n):
    a=int(input())
    b.append(a)
    p+=a
def fun(c,add,r):
    global q
    d=c[:]
    if(q==1 or len(c)<=1):
        return
    for i in range(r):
        print(len(c),i)
        t2=c.pop(i)
        add+=t2
        t=add
        if(add==sum(c)):
            q=1
            return
        for j in range(len(c)):
            t1=c[j]
            c[j]=0
            if(t+t1 == sum(c)):
                q=1
                c[j]=t1
                return
            c[j]=t1
        fun(c,add,len(c))
        add-=t2
        c.insert(i,t2)
if(p==360):
    print("YES")
else:    
    fun(b,0,n)
    if(q==1):
        print("YES")
    else:
        print("NO")
