#https://www.codechef.com/problems/R5S?tab=statement

num , rate = map(int , input().split())

current = num + rate

if current >= 2000:
    print("YES")
else:
    print("NO")    