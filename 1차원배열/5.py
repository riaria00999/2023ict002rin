N, M = map(int, input().split())

baskets = [0] * N
for i in range(M):
    i, j, k = map(int, input().split())
    for basket in range(i-1, j):
        baskets[basket] = k

print(*baskets)
