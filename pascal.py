r=int(input("enter number of rows:"))
for i in range(r):
    for l in range(0,r-i):
        print(end="  ")
    for j in range(0,i+1):
        if j==0 or i==0:
            c=1
            print(c,end="   ")
        else:
            c=(int)(c*(i-j+1)/j)
            print(c,end="   ")
    print()        
            
