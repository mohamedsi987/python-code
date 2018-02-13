#decimal to binary
x=int(input())
a=[]
while x>0 :
    b=x%2
    if b==0:
        a.append (0)
        print(0)
    else:
        a.append (1)
        print(1)
    x=x//2
    
       
            
