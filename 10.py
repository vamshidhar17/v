def push():
   print("enter element to push")
   q=int(input())
   top=top+1
   stack[top]=q

def pop():
   l=stack[top]
   top=top-1
   return l

def display():
   top=-1
   while top<=max:
   	 print(stack[top])

def main():	
   top=-1
   stack=[]
   print("enter number of elements do u wany in stack")
   max=int(input())
   p="y"
   while p=="y":
    print("enter ur choice")
    print("1.push")
    print("2.pop")
    print("3.display")
    print("4.exit")
    m=int(input())
    if m==1:
      push()
    elif m==2:
     print(pop())
    elif m==3:
     diplay()
    else:
     break
    print("do u wnat to continue")
    p=input()  
if "__main__"=="__name__":
   main()	
	
	
	
	
