n=int(input())
i=1
while True:
   if n%i==0 and (n//i)%2==1:
   	print(i)
   	break
   else:
   	i=i+1
