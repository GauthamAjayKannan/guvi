n=int(input())
l=list(map(int,input().split(" ")))
coun=0
for i in range(len(l)):
	if (i+1)*n in l:
		coun+=1
print(coun)
