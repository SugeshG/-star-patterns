#increasing triangle 
n=5
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print() 
print()    
#decreasing triangle pattern
n=5
for i in range(n):
    for j in range(n-i):
        print("*",end=" ")
    print() 