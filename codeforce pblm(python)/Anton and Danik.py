#https://codeforces.com/problemset/problem/734/A

lt = int(input())
s = input()
a = s.count("A")
d = s.count("D")
if a > d :
    print("Anton")
elif d > a:
    print("Danik")
else:
    print("Friendship")        