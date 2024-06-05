#https://www.codechef.com/practice/course/arrays-strings-sorting/INTARR01/problems/MISSP?tab=statement

t = int(input())
for i in range(t):
    lt = int(input())
    ls = []
    for j in range(lt):
        ls.append(int(input()))
            
    for j in ls:
        if ls.count(j) % 2 == 1 :
            print(j)
            break        
    