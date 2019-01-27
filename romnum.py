#numrom
n=input()
rom=['I','II','III','IV','V','VI','VII','VIII','IX','X']
n=n if n in rom else list(n)
n=rom.index(n)+1 if isinstance(n,str) else sum([rom.index(i)+1 for i in n if i in rom])
print(n)
