#sortlength
n=input()
s=input().split(" ")
s.sort()
print(*sorted(s,key=len))
