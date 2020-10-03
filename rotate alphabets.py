n = int(input())
s = input()
rot = int(input())
for i in s:
    if i.islower():
        i = chr((ord(i) - 97 + rot)%26 + 97)
    elif i.isupper():
        i = chr((ord(i) - 65 + rot)%26 + 65)
    print(i, end='')
