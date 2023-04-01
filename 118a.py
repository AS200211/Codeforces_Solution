n = input()
n = n.lower()
n = n.replace('a','')
n = n.replace('e','')
n = n.replace('i','')
n = n.replace('o','')
n = n.replace('u','')
n = n.replace('y','')
a = ''
for i in n:
    a+='.'
    a+=i
print(a)