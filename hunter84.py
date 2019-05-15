s=input()
r=""
n=0
count=1
while n<len(s):
	t=s[n]
	if n+1<len(s) and s[n]==s[n+1]:
		count+=1
	elif n==len(s)-1 and s[len(s)-1]!=s[len(s)-2]:
		r+=s[len(s)-1]
	else:
		if count>1:
			r+=str(count)+"*"+t
			count=1
		else:
			r+=t
	n+=1
print(r)
