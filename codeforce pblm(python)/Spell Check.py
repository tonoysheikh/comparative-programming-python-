#https://codeforces.com/problemset/problem/1722/A

t = int(input())
for i in range(t):
    lt = int(input())
    s = input()
    ls1 = list(s)
    ls1.sort()
    name = "Timur"
    ls2 = list(name)
    ls2.sort()
    
    if ls1 == ls2 :
        print("YES")
    else:
        print("NO")