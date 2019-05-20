wl=list(map(int,input().split(" ")))
vl=list(map(int,input().split(" ")))
fin=False
d=[(vl[i],wl[i]) for i in range(len(wl))]
for i in range(len(vl)):
	sum,we=0,0
	for j in range(i,len(vl)):
		sum+=d[j][0]
		we+=d[j][1]
		if we==w:
			fin=True
			break
		elif we>w:
			break
	if fin==True:
		break
print(sum)
