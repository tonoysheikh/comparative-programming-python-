#https://codeforces.com/problemset/problem/25/A

lt = int(input())
ls = list(map(int,input().split()))

odd = 0
even = 0
for i in range(lt):
    if ls[i] % 2 == 0:
        evenIndex = i
        even += 1
    else :
        oddIndex = i
        odd += 1

if even == 1:
    print(evenIndex+1)
else:
    print(oddIndex+1)              
        
    
 
  