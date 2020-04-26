n=int(input())
d=dict()
for _ in range(n):
    a,b=input().split()
    d[a]=int(b)

for j in range(n):
    e=input()  
    try:
        d[e]+=0
        print(e,"=",d[e],sep="")
    except:
        print("Not found")      
