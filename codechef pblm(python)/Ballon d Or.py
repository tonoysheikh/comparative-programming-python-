#https://www.codechef.com/problems/BLNDOR?tab=statement
t = int(input())
for i in range(t):
    lt = int(input())
    ls = list(map(int,input().split()))
    
    cnt = ls.count(2)
    if cnt % 8 == 0:
        print("YES")
    else:
        print("NO")    