#numrom
n=list(input())
rom=['I','II','III','IV','V','VI','VII','VIII','IX','X']
n=[rom.index(i)+1 for i in n if i in rom]
print(sum(n))
