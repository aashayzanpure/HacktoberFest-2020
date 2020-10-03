

n = int(input()) # Change the alphabets of string by a specific factor i.e. if string is 'abc' and factor is 3, then each letter is shifted ahead by 3 , i.e. it will become 'def'
s = input()
rot = int(input())
for i in s:
    if i.islower():
        i = chr((ord(i) - 97 + rot)%26 + 97)
    elif i.isupper():
        i = chr((ord(i) - 65 + rot)%26 + 65)
    print(i, end='')

import math # Print sum of n prime numbers
limit = int(input())
n = 2
count, sum = 0, 0
while count < limit:
	flag = True
	for i in range(2, (int)(math.sqrt(n))+1):
		if n%i == 0:
			flag = False
			break
	if flag == True:
		sum = sum + n
		count += 1
	n += 1
print(sum)


