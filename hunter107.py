s=input()
r=""
for i in range(len(s)-1):
	for j in range(i+1,len(s)):
		t=s[i:j+1]
		t=t[::-1]
		if s[i:j+1]==t:
			if len(s[i:j+1])>len(r):
				r=s[i:j+1]
if r=="":
	print(1)
else:
	print(len(r))
