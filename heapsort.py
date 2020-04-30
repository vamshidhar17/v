def heapify(a,n,i):
    l = 2*i +1
    r = 2*i +2
    lar=i
    if(l<n and a[lar] < a[l]):
        lar=l
    if(r<n and a[lar] < a[r]):
        lar=r
    if(lar!=i):
        (a[lar],a[i])=(a[i],a[lar])
        heapify(a,n,lar)
def hs(a):
    n=len(a)
    for i in range(int(n/2),-1,-1):
        heapify(a,n,i)
    for i in range(n-1,-1,-1):
        (a[0],a[i])=(a[i],a[0])
        heapify(a,i,0)
a=list(map(int,input().split()))
hs(a)
print(*a)
        
        
