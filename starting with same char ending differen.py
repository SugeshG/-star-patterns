#starting with same char ending different char on each line    
n=5
for i in range(n):
    p=65
    for j in range(i+1):
        print(chr(p),end=" ")
        p=p+1    
    print()     