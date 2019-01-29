#greatestdivnum
n=list(map(int,input().split(" ")))
ma=max(n)
while ma>0:
	if n[0]%ma==0 and n[1]%ma==0:
		print(ma)
		break
	ma=ma-1
