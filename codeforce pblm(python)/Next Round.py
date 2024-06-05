#https://codeforces.com/contest/158/problem/A

lt , place = map(int , input().split())
ls = list(map(int , input().split()))

finish = ls[place-1]
cnt = 0
for i in ls:
    if i >= finish and i > 0:
        cnt+=1
        
print(cnt)            