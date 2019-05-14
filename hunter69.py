s=input()
che=True
if '@' not in s:
	che=False
if s.count('@')>1 or s.count('.')>1 and che==True:
	che=False
if len(s[s.index('@'):s.index('.')+1])<4 and che==True:
	che=False
if len(s[:s.index('@')])<3 and che==True:
	che=False
if s.endswith('.com')==False and che==True:
	che=False
if che:
	print("YES")
else:
	print("NO")
