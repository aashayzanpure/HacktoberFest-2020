array = list(map(int, input().split()))
flag  = True
maxi, count = 0, 0
for i in array:
	if i == 1:
		count += 1
		maxi = max(maxi, count)
	else:
		count = 0
print(maxi)