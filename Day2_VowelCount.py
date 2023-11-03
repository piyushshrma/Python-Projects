a=input("Enter String:")
l=len(a);
A=0;
E=0;
I=0;
O=0;
U=0;
for i in a:
    if(i=='a' or i=='A'):
        A+=1;
    elif(i=='E' or i=='e'):
        E+=1;
    elif(i=='I' or i=='i'):
        I+=1;
    elif(i=='o' or i=='O'):
        O+=1;
    elif(i=='U' or i=='u'):
        U+=1;    
print("A: ",A);
print("E: ",E);
print("I: ",I);
print("O: ",O);
print("U: ",U);
