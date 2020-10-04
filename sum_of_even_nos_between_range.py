lower = int(input())
upper = int(input())
sum0 = 0
for i in range(lower, upper+1):
	if i%2 == 0:
		sum0 = sum0 + i
print(sum0)