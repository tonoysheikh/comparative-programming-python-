#https://codeforces.com/problemset/problem/1676/A

t = int(input())
for i in range(t):
    s = input()
    ls = list(map(int , s))
    if sum(ls[0:3]) == sum(ls[3:]):
        print("YES")
    else:
        print("NO")        
    
    