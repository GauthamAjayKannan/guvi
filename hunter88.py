n,k=list(map(int,input().split(" ")))
s="".join(input().split(" "))
coun=0
ini=0
start=False
for i in range(len(s)):
	if s[i]=='*' and start==False:
		ini=i
		start=True
	elif s[i]=='*' and start==True:
		if len(s[ini:i+1])<=k:
			coun+=1
		else:
			coun+=2
		start=False
if start==True:
	coun+=1
print(coun)
