def inte(n):
    sum=0
    while n!=0:
        m=n%10
        sum= (sum*10)+m
        n=int(n/10)
    return(sum)
n=int(input("enter num to reverse"))
p=inte(n)
print(p)
