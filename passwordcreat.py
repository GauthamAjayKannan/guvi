s1,s2=input().split(" ")
r=""
while s1!="" and s2!="":
	r+=s1[0]+s2[0]
	s1=s1[1:]
	s2=s2[1:]
a=1
if s1!="":
	while s1!="":
		r+=s1[0]
		r+=str(a)
		s1=s1[1:]
		a+=1
else:
	while s2!="":
		r+=str(a)
		r+=s2[0]
		s2=s2[1:]
		a+=1
print(r)
