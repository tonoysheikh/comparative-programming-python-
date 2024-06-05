#https://codeforces.com/problemset/problem/1850/A

t = int(input())
for i in range(t):
    ls = list(map(int , input().split()))
    ls.sort()
    if ls[1]+ls[2] >= 10:
        print("YES")
    else:
        print("NO")    