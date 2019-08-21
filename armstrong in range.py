
for i in range(1,1001):
    s=0
    n1=i
    n=len(str(i))
    
    while(i!=0):
        r=i%10
        s=s+r**n
        
        i=i//10
    if(n1==s):
     print(s)

       
    
