def fun(q):
    global q2,c
    if(len(q)!=1):
        for i in range(len(q)):
           x=q.pop(i)
           q2.append(x)
           fun(q)
           q2.pop(-1)
           q.insert(i,x)
    else:
        q2.append(q[0])
        ct=0
        print(q2)
        for k in range(n):
            if(((q2[k]%(k+1)==0)or((k+1)%q2[k])==0)):
                ct+=1
            if(ct==n):
                c+=1
        q2.pop(-1)



c=0
q2=[]
q=[]
n=int(input())
for j in range(1,n+1):
    q.append(j)
    
q1=q[:]
fun(q)
print(c)

