# time
n=int(input())
h,s=0,0
if n<60:
	h=0
	s=n
else:
	h=n//60
	s=n%60
print(h,s)
