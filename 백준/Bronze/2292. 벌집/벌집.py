n = int(input())
numbox, cnt = 1, 1

while n > numbox:
    numbox += 6 * cnt
    cnt += 1
print(cnt)