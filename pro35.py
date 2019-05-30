s=input()
l=list(set(s))
le=2
a=0
check=False
while True:
    ch=l[a]
    for j in range(0,len(s)-le):
        if ch in s[j:j+le]:
            check=True
        else:
            check=False
            a+=1
            if a>=len(l):
             a=0
             le+=1
            break

    if check==True:
        break
print(le)
