class node:
    def __init__(self,data):
        self.data=data
        self.a=[]
class generaltree:
    def __init__(self,head):
        self.temp=head
    def findparent(self,c,p,node):
        temp1=self.temp
        st=[]
        while(temp1.data!=p):
            st.extend(temp1.a)
            print(temp1.data)
            temp1=st.pop(0)
        if(temp1.data==p):
            temp1.a.append(node)
t=int(input())
p,c=map(int,input().split())
head=node(p)
tree=generaltree(head)
newnode=node(c)
tree.findparent(c,p,newnode)
for _ in range(t-1):
    p,c=map(int,input().split())
    newnode=node(c)
    tree.findparent(c,p,newnode)

    
        
