 que=[]
def push(f,r,n,que):
   print("enter element to insert")
   q=int(input())
   if f==0 and r==n or (r==f-1):
     print("que is full")
   elif f==-1:
     f=0
     r=0	
   elif f<r and r==n-1:	 
     r=0
   else:
     r=r+1
     que.insert(r,q)
	 
def pop():
    p=que[0]
    del(que[0])
    return p   

def display(que):
   top=len(que)
   print("elements in que are")
   print(que)	 
f=-1
r=-1
print("enter number of elements do u wany in que")
n=int(input())
p="y"
while p=="y":
  print("enter ur choice")
  print("1.insert")
  print("2.delete")
  print("3.display")
  print("4.exit")
  m=int(input())
  if m==1:
    push(f,r,n,que)
  elif m==2:
   print("deleted is",pop())
  elif m==3:
   display(que)
  else:
   break
  print("do u wnat to continue")
  p=input()   
	
