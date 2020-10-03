n = input()
l = list(n)
for i in l:
    n = n.replace(i*2,'')
print("Empty String" if n == '' else n)
