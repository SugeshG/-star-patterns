count=int(input("enter the no: "))
width=int(input("enter the no: "))
for i in range(10):
    print(("*"*count).center(width))
    count=count+2 
print("| |".center(width))    
