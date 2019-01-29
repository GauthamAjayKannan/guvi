#ENCODE
n=list(input())
n=[chr(ord(i)+3)if ord(i)<=ord("W") else chr(ord("A")+(ord(i)+2)-ord("Z")) for i in n]
print("".join(n))
