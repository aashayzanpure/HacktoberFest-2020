num = int(input()) # Program to write first 'num' numbers of fibonacci series
a, b = 0, 1
c, n = int(), int()
print("0", " ", end = "")
while n < num-1:
	print(b, " ", end = "")
	c = a
	a = b
	b = c + b
	n += 1

# 0	1	1	2	3	5	8	13