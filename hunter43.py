s=input()
r,t="",""
i=0
while i<len(s):
    if s[i].isalpha():
        t=s[i]
        i+=1
    elif s[i].isnumeric():
        n=""
        while i<len(s) and s[i].isnumeric():
            n+=s[i]
            i+=1
        if int(n)%2==0:
            r+=t*int(n)
        else:
            r+=(t+n)
print(r)
