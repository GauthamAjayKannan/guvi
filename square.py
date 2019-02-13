pt=[list(map(int,input().split(" "))) for i in range(4)]
l=[((pt[i+1][1]-pt[i][1])**2+(pt[i+1][0]-pt[i][0])**2)**1//2 for i in range(len(pt)-1)]
l.append(((pt[len(pt)-1][1]-pt[0][1])**2+(pt[len(pt)-1][0]-pt[0][0])**2)**1//2)
for i in l:
	if i%l[0]!=0:
		print("no")
		break
else:
	print("yes")
