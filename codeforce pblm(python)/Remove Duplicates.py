#https://codeforces.com/problemset/problem/978/A

lt = int(input())
ls = list(map(int , input().split()))

a=[]

for i in ls:
	while i in a:
		del a[a.index(i)]
	a.append(i)
print(len(a))
print(*a)
 	 		 	 	  	  	 	    	  		 				