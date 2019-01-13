#odddigits
n=list(input())
n=[i for i in n if int(i)%2==1]
print(*n)
