n=input()
count=0
for i in n:
    if i==" " or i.isalpha() or i.isnumeric():
        pass
    else:
        count=count+1
print(count)
