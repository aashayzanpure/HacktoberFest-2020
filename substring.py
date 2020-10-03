n = int(input())
phrase = "hackerrank"

for i in range(n):
    s = input().strip()
    p = 0
    for j in s:
        if j == phrase[p]:
            p += 1
        if p == len(phrase):
            break
    if p == len(phrase):
        print('YES')
    else:
        print('NO')
        
