n = int(input())
total = 0
while n != 0:
	a = n % 10
	n = int(n / 10)
	total = total + a
print(total)