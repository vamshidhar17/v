def push(que): 
   if len(que)<=n-1:
     print("enter element to insert")
     q=int(input())
     que.append(q)
     top=len(que)	 
   else:
     print("que overflow")   

def pop():
   l=len(que)
   if l!=0:
      p=que[0]
      del(que[0])
      return p
   else:
      print("there is no element to delete")

def display(que):
   top=len(que)
   print("elements in que are")
   print(que)
   	 
que=[]
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
    push(que)
  elif m==2:
   print("deleted is",pop())
  elif m==3:
   display(que)
  else:
   break
  print("do u wnat to continue")
  p=input()   
	
