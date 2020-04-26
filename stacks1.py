def push(stack): 
   print(n)
   if len(stack)<=n-1:
     print("enter element to push")
     q=int(input())
     stack.append(q)
     top=len(stack)	 
   else:
     print("stack overflow")   

def pop():
    top=len(stack)
    if top>0:
       p=stack[top-1]
       del(stack[top-1])
       top-=1
       return p 
    else:
       print("stack underflow")	

def display(stack):
   top=len(stack)
   print("elements in stack are")
   print(stack)
   	 
stack=[]
print("enter number of elements do u want in stack")
n=int(input())
p="y"
while p=="y":
  print("enter ur choice")
  print("1.push")
  print("2.pop")
  print("3.display")
  print("4.exit")
  m=int(input())
  if m==1:
    push(stack)
  elif m==2:
   print("deleted is",pop())
  elif m==3:
   display(stack)
  else:
   break
  print("do u want to continue")
  p=input()   
	
