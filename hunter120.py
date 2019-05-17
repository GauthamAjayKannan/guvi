n=input()
l=list(map(int,input().split(" ")))
coun=0
for i in range(0,len(l)-2):
	for j in range(i+1,len(l)):
		if l[i]+l[j] in l[j+1:]:
			coun+=1
print(coun)
