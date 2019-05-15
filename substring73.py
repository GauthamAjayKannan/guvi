s1=input()
s2=input()
r=[]
n=0
for i in range(len(s2)-1):
	for j in range(i,len(s2)):
		if s2[i:j+1] in s1:
			r.append(s2[i:j+1])
print(max(r,key=len))
