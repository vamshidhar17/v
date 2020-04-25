import random
mat=[]
mat2=[]
mat4=[]
for i in range(1,26):
    mat.append(i)
bingo=["B","I","N","G","O"]
mat12=[]
mat12=mat[ : ]
def ply1():
    mat1=mat[ : ]
    
    for i in range(1,6):
        l=[]
        for j in range(1,6):
            p=True
            while p==True:
                print("enter the number at("+str(i)+","+str(j)+")")
                a=int(input())
                if a>25:
                    print("enter a number less than 25 and not repeated")
                x=0
                while x<len(mat1):
                    if a==mat1[x]:
                        p=False
                    x=x+1
                if p==True and a<25:
                    print("sorry you have entered a repeated number")
                
            print(a,end="\t")
            l.append(a)
            mat1.remove(a)
            print()
        print()
        mat2.append(l)
    for i in range(0,5):
        for j in range(0,5):
            print(mat2[i][j],end="\t")
        print()
        print()
        print()
       
def game1(c):
    k=[]
    for i in range(0,5):
        for j in range(0,5):
            if c==mat2[i][j]:
                mat2[i][j]="o"
    for i in range(0,5):
        for j in range(0,5):
            print(mat2[i][j],end="\t")
        print()
        print()
        print()
    bing=bingo[ : ]
    for t in range(0,5):
        T=0
        T1=0
        T2=0
        T3=0
        for j in range(0,5):
            
            if mat2[t][j]=="o":
                T=T+1
            if mat2[j][t]=="o":
                T1=T1+1
            if t==j:
                if mat2[t][j]=="o":
                    T2=T2+1
            if T==5:
                m1=bing[0]
                k.append(m1)
                bing.remove(m1)
            if len(bing)==0:
                print(k)
                print("congratulations")
                print("YOU WON THE MATCH")
                return False     
            if T1==5:
                m1=bing[0]
                k.append(m1)
                bing.remove(m1)
            if len(bing)==0:
                print(k)
                print("congratulations")
                print("YOU WON THE MATCH")
                return False    
                
            if T2==5:
                m1=bing[0]
                k.append(m1)
                bing.remove(m1)
            if len(bing)==0:
                 print(k)
                 print("congratulations")
                 print("YOU WON THE MATCH")
                 return False   
        for q in range(0,5):
            if mat2[q][4-q]=="o":
                T3=T3+1
        if T3==5:
            m1=bing[0]
            k.append(m1)
            bing.remove(m1)
    if len(bing)==0:
        print(k)
        print("congratulations")
        print("YOU WON THE MATCH")
        return False
    else:
        return True       
               
def ply2():
    mat3=mat[ : ]
    for i in range(1,6):
        l=[]
        for j in range(1,6):
            a=random.choice(mat3)
            l.append(a)
            mat3.remove(a)
        mat4.append(l)   
def game2(c1):
    k1=[]
    mat5=[]
    mat5=mat[ : ]
    mat5.remove(c1)
    for i in range(0,5):
        for j in range(0,5):
            if c1==mat4[i][j]:
                mat4[i][j]="o"       
    bing1=bingo[ : ]
    for t in range(0,5):
        T=0
        T1=0
        T2=0
        T3=0
        for j in range(0,5):
            
            if mat4[t][j]=="o":
                T=T+1
            if mat4[j][t]=="o":
                T1=T1+1
            if t==j:
                if mat4[t][j]=="o":
                    T2=T2+1
            if T==5:
                m1=bing1[0]
                k1.append(m1)
                bing1.remove(m1)
            if len(bing1)==0:
                print(k1)
                print("YOU LOST THE MATCH")
                print("BETTER LUCK NEXT TIME")
                return False 
            if T1==5:
                m1=bing1[0]
                k1.append(m1)
                bing1.remove(m1)
            if len(bing1)==0:
                print(k1)
                print("YOU LOST THE MATCH")
                print("BETTER LUCK NEXT TIME")
                return False
            if T2==5:
                m1=bing1[0]
                k1.append(m1)
                bing1.remove(m1)
            if len(bing1)==0:
                print(k1)
                print("YOU LOST THE MATCH")
                print("BETTER LUCK NEXT TIME")
                return False
        for q in range(0,5):
            if mat4[q][4-q]=="o":
                T3=T3+1
        if T3==5:
            m1=bing1[0]
            k1.append(m1)
            bing1.remove(m1)
    if len(bing1)==0:
        print(k1)
        print("YOU LOST THE MATCH")
        print("BETTER LUCK NEXT TIME")
        return False
    else:
        return True       
                       
            
print("do u want to start the game first?y or n")
b=input()
if b=="y":
    n=ply1()
    n1=ply2()
    n2=True
else:
   n=ply2()
   n1=ply1()
   n2=False
if n2==True:
    k5=True
    while k5==True:
        m6=int(input("enter your choice: "))
        mat12.remove(m6)
        k5=game1(m6)
        if k5==True:
            k5=game2(m6)
            m6=random.choice(mat12)
            mat12.remove(m6)
        if k5==True:
            k5=game2(m6)
        if k5==True:
            k5=game1(m6)
         
else:
    k5=True
    while k5==True:
        m6=random.choice(mat12)
        mat12.remove(m6)
        k5=game2(m6)
        if k5==True:
            k5=game1(m6)
        if k5==True:
            m6=int(input("enter your choice : "))
            mat12.remove(m6)
            k5=game1(m6)
        if k5==True:
            k5=game2(m6)
        
    
    
    
    
        
    
    
    
    
            
    
        
