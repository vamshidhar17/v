'''n=int(input())
d=dict()
s=0
for i in range(n):
    j=input()
    try:
        d[j]+=1
    except:
        d[j]=1
        s+=1
print(s)
l=list(d.values())
l.sort()
d.clear()
for j in range(len(l)-1,-1,-1):
    print(l[j],end=" ")        '''
n=int(input())
for _ in range(n):
    q=int(input())
    s=0
    a = list(map(int,input().split()))
    if(a[0]>=a[-1]):
        k1=a[-1]
    else:
        k1=a[0]    
    for i in range(q):
        if(a[i]>=a[q-(i+1)] and i<=(n-i-1)):
            if(k1>=a[i]):
                k1=a[q-(i+1)]
                s+=1
            if(s==int(n/2) or s==int((n-1)/2)):
                break
        elif(a[i]<=a[q-(i+1)] and i<=(n-i-1)):
            if(k1>=a[q-i-1]):
                k1=a[i]
                s+=1
            if(s==int(n/2) or s==int((n-1)/2)):
                break
        else:
            #print(s)
            print("No")
            break
    if(s==int(n/2) or s==int((n-1)/2)):
        print("Yes")
    a.clear()    



