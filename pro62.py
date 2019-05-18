s=input()
r=""
for i in range(len(s)-1):
	for j in range(i+1,len(s)):
		t=s[i:j+1]
		t=t[::-1]
		if t==s[i:j+1]:
			if len(r)<=len(t):
				r=t
print(len(s)-len(r))
