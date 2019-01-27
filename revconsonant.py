#reverseconsonant
s=list(input())
s=[i for i in s if i not in ['a','e','i','o','u']]
print("".join(s[::-1]))
