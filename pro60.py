n=int(input())
time,value=1,3
inivalue=3
while True:
    time+=1
    if value==1:
           value=inivalue*2
           inivalue=value
    else:
           value-=1
    if time==n:
		   print(value)
		   break
