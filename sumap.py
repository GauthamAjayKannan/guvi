#ap
a,b,c=list(map(int,input().split(" ")))
re=0
for i in range(1,c+1):
	s=a+(i-1)*b
	re=re+s
print(re)
