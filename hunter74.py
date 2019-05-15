###hunter
s1=input()
s2=input()
t=""
ini,fi=0,0
r=[]
n=0
for i in range(len(s2)-1):
	for j in range(i,len(s2)):
		if s2[i:j+1] in s1:
			if len(s2[i:j+1])>=len(t):
				t=s2[i:j+1]
				ini=i
				fi=j
print(s2[ini:fi+1])
