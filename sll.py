class Node:
   def __init__(self,data):
    self.data=data
    self.next=None 
class s_list:
   def __init__(self):
     self.head=None  
   def insert_beg(self,data):
    node=Node(data)
    if self.head==None:
     self.head=node
    else :
     node.next = self.head
     self.head = node
    print("node inseted")
    return
   def insert_pos(self,data,pos):
    node = Node(data)
    if pos==0:
     self.insert_beg(data)
    else:
       temp=self.head
       i=0
       while i<=pos-1:
        temp=temp.next
       node.next=temp.next
       temp.next=node
  def insert_end(self,data):	 
    node=Node(data)
    temp=self.head
    i=0
    while(temp.next is not None):
     temp=temp.next	
   temp.next=node
   return
def menu()
  print("1.insert at beginning")
  print("2.insert at position")
  print("3.insert at end")
  print("4.del at beginning")
  print("5.del at position")
  print("6.del at end")
  print("7.display")
  print("8.count")
  print("9.exit")
  ch=eval(input("enter u choice"))
  return ch
print("______single linked list______")
l = s_list()
while True:
  ch=menu()
  if ch==1:
   data=int(input("enter data"))
   l.insert_beg(data)
  elif ch==2:
   data=int(input("enter data"))
   pos=int(input("enter data"))
   l.insert_pos(data,pos)
  elif ch==3:
   data=int(input("enter data"))
   l.insert_end(data)
  else:
   break
