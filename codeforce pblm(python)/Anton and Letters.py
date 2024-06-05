#https://codeforces.com/problemset/problem/443/A

s = input()
ls = []
for i in s:
    if i.isalpha():
        ls.append(i)
           
uniqueValue = list(set(ls))
print(len(uniqueValue))  
   