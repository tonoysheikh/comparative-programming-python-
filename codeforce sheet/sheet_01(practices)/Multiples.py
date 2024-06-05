x , y = map(int,input().split()) 

if(x >= y and x%y == 0):
    print("Multiples")
elif(y >= x and y%x == 0):
    print("Multiples")
else:
    print("No Multiples")