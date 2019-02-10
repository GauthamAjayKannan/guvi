#palin
s=input().lower()
r=[]
if s==s[::-1]:
	r.append(s)
	s=s[1:]
while len(s)!=1:
	for i in range(1,len(s[1:])):
		if s[0]==s[i]:
			print("end",s[i])
			u=s[:i+1]
			print("u is",u)
			if s[:i+1]==u[::-1]:
				r.append(u)
	s=s[1:]
print(*r)
