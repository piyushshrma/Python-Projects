x=0;
y=0;
while(x!=2):
    rn = int(input("Enter the rule number:"))
    if(rn==1):
        if(x<4):
            x=4
        print("x ",x)
        print("y ",y)
        
    elif(rn==2):
        if(y<3):
            y=3
        print("x ",x)
        print("y ",y)
        
    elif(rn==3):
        if(x>0):
            d=int(input("How much water you want to remove from 4 G jug:"))
            x=x-d;
        print("x ",x)
        print("y ",y)
        
    elif(rn==4):
        if(y>0):
            d=int(input("How much water you want to remove from 3 G jug:"))
            y=y-d;
        print("x ",x)
        print("y ",y)
        
    elif(rn==5):
        if(y>0):
            x=0;
        print("x ",x)
        print("y ",y)
        
    elif(rn==6):
        if(y>0):
            y=0;
        print("x ",x)
        print("y ",y)
        
    elif(rn==7):
        if (x+y)>=4 and y>0:
            x=4;
            y=y-(4-x);
        print("x ",x)
        print("y ",y)
        
    elif(rn==8):
        if((x+y)>=3 and x>0):
            x=x-(3-y);
            y=3;
        print("x ",x)
        print("y ",y)
        
    elif(rn==9):
        if((x+y)<=4 and y>0):
            x=x+y;
            y=0;
        print("x ",x)
        print("y ",y)
        
    elif(rn==10):
        if((x+y)<=3 and x>0):
            x=0;
            y=x+y;
        print("x ",x)
        print("y ",y)
        
    elif(rn==11):
        if(x==0 and y==2):
            x=2;
            y=0;
        print("x ",x)
        print("y ",y)
        
    elif(rn==12):
        if(x==2):
            x=0;
        print("x ",x)
        print("y ",y)
        
    else:
        print("Invalid choice");
