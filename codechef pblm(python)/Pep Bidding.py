#https://www.codechef.com/problems/BID?tab=statement

t = int(input())

for i in range(t):
    lt = int(input())
    aattack = list(map(int , input().split()))
    adefence = list(map(int , input().split()))
    pattack = list(map(int , input().split()))
    pdefence = list(map(int , input().split()))
    
    aa = sum(aattack)
    ad = sum(adefence)
    pa = sum(pattack)
    pd = sum(pdefence)
    
    if aa > pa and ad > pd:
        print("A")
    elif aa < pa and ad < pd:
        print("P")
    else :
        print("DRAW")        
    