 r=[]
    n=int(input('enter the no. of lines'))
    r.append('*')
    r.append('**')
    s=1
    sta=3
    if n%2:
        sta=2
    for i in range(sta,n//2+1):
        r.append('*'+" "*s+"*")
        s+=1
    for i in r:
        print(i)
    if n%2:
        r=r[:len(r)-1]
    r=r[::-1]
    for j in r:
        print(j)
