N, M = map(int, input().split())

set_S = set()
for _ in range(N):
    string = input().strip()
    set_S.add(string)

count = 0
for _ in range(M):
    string = input().strip()
    if string in set_S:
        count += 1
print(count)
