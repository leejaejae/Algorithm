import sys
input = sys.stdin.readline

n = int(input())
li = []
for _ in range(n):
    [x, y] = map(int, input().split())
    li.append([x, y])

li.sort()
for i in li:
    print(i[0], i[1])