s=input()
inp=input()
if len(s[:s.index('|')]+inp)==len(s[s.index('|')+1:]):
	print(s[:s.index('|')+1]+inp+s[s.index('|')+1:])
elif len(s[:s.index('|')])==len(s[s.index('|')+1:]+inp):
	print(s+inp)
else:
	print("Impossible")
