#smallestdivisiblenum
n=list(map(int,input().split(" ")))
v=min(n)
while True:
	if v%n[0]==0 and v%n[1]==0:
		print(v)
		break
	v=v+1
