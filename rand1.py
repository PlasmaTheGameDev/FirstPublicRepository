a=int(input("Enter The Number of Rs.1 coin"))
b=int(input("Enter The Number of Rs.5 coin"))
c=int(input("Enter The Amount to be Paid"))

x=0
y=0
total=0
flag=0

while total!=c:
    if b!=0:
        total+=5
        if total>c:
            total-=5 
            b=0
        else:
            y+=1
            b-=1

    elif a!=0:
        total+=1
        if total>c:
            total-=1
            flag=1
            
        else:    
            x+=1
            a-=1

    if a==0 and b==0:
        total=c
        flag=1


            
if flag==1 :
    print(-1)
else:
    print(x,y)
