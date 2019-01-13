#mid*
s=list(input())
if len(s)%2:
	s[len(s)//2]="*"
else:
	s[(len(s)//2)-1]="*"
	s[len(s)//2]="*"
print("".join(s))
