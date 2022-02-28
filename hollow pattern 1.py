n=5
for i in range(n):
    for j  in range(i+1):
        if(j==0 or i==n-1 or j==i):
            print("*",end=" ")
        else:
            print(" ",end=" ")                
    for j in range(1,n-i): 
        print(" ",end=" ")
    for j in range(1,n-i):
        print(" ",end=" ")        
    for j in range(i+1):
        if(j==0 or j==i or i==n-1):
          print("*",end=" ")  
        else:
            print(" ",end=" ")
    print()                            
