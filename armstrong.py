limit = int(input())
count = 0
i = 0
while count < limit:
	origin = i
	cube = 0
	while i != 0:
		a = i % 10
		cube = cube + (a ** 3)
		i = int(i / 10)
	if cube == origin:
		print(cube)
		count += 1
	i += 1