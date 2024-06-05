t = int(input())
for t in range(t):
    
    s = input()
    lt = len(s)
    
    if lt % 2 == 0 and s[0] != ')' and s[lt-1] != '(':
        print("YES")
    else:
        print("NO")