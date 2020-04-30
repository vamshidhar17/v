n=int(input())
s=input()
t=input()
def mp(A,B):
    m = len(A)
    n = len(B)
    if(n!=m):
        return -1
    c = [0] * 256
    for i in range(n):
        c[ord(B[i])]+=1
    for i in range(n):
        c[ord(A[i])]-=1
    for i in range(256):
        if c[i]:
            return -1
    s1=list(A)
    s2=list(B)
    r=[]
    i=0
    j=0
    while(i<len(s1)):
        j=i
        while(s1[j]!=s2[i]):
            j+=1
        while(i<j):
            s1[j],s1[j-1]=s1[j-1],s1[j]
            r.append(j)
            j-=1
        i+=1
    return r
o=mp(s,t)
if(o==-1):
    print(-1)
else:
    print(len(o))
    print(*o)
