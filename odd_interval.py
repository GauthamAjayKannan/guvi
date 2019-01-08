#odd series
s,e=list(map(int,input().split(" ")))
for i in range(s+1,e):
	if i%2==1:
		print(i,end=" ")
