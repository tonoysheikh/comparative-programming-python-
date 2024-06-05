#https://www.codechef.com/problems/MOOCHEF?tab=statement

t = int(input())
for i in range(t):
    lt , l , h = map(int , input().split())
    data = list(map(int, input().split()))
    
    sum = 0
    mini = 0
    maxi = 0
    
    for j in data:
        if j >= l and j <= h:
            sum = sum + 1
            maxi = max(sum , maxi)
        else:
            sum = sum - 1 
            mini = min(sum , mini)
               
    print(maxi,mini)        