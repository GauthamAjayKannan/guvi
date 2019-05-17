s=input().split(" ")
tmin=min(s,key=len)
tmax=max(s,key=len)
r=""
for i in range(len(tmin)-1):
	for j in range(i+1,len(tmin)+1):
		if tmin[i:j] in tmax:
			if len(r)<len(tmin[i:j+1]):
				r=tmin[i:j]
print(r)
