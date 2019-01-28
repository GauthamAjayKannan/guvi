#firstrepeatednum
n=int(input())
l=list(map(int,input().split(" ")))
m=[0]*10
for i in l:
	m[i-1]=m[i-1]+1
	if 2 in m:
		print(m.index(2)+1)
		break
if 2 not in m:
	print("unique")
