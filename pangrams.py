alpha = 'abcdefghijklmnopqrstuvwxyz '
s = input().lower()
flag = 0
for i in alpha:
    if i not in s:
        print("not pangram")
        flag = 1
        break
if flag == 0:
    print("pangram")