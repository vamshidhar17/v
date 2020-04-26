def getinteger(a):
   f=input("enter element to search")
   n=len(a)
   print(n) 
   i=0
   while i<n:
    if a[i]==f:
      return f	
    i=i+1
   print("element not found") 
def main():
  print(" enter the num of array elements")
  q=int(input())  
  print("started,enter list")
  a=[]
  for i in range(q):
    print(i+1)
    L=int(input("enter element"))
    a.append(L)
  
  o=getinteger(a)
  print("element found",o)
  
if __name__=="__main__":
  main()
