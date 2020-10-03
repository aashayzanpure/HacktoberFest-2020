string = input() # Take input until a blank line is occurred
s = list()
nos = list()
while True:
    line = input()
    if line:
        s.append(line)
    else:
        break
print(s)