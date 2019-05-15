n=int(input())
count=0
l=[]
for i in range(n+1):
	check=False
	if len(str(i))==1:
		count+=1
	else:
		for j in range(len(str(i))-1):
			te=str(i)
			if abs(int(te[j])-int(te[j+1]))==1:
				check=True
			else:
				check=False
				break
		if check==True:
			count+=1
print(count)
