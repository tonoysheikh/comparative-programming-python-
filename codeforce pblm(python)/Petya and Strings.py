#https://codeforces.com/problemset/problem/112/A

s1 = input()
s2 = input()
s1 = s1.upper()
s2 = s2.upper()
if s1 > s2:
    print("1")
elif s1 < s2:
    print("-1")
else:
    print("0")        