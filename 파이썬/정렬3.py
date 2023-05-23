N, k = map(int, input().split())

scores = list(map(int, input().split()))

scores.sort(reverse=True)

cutoff = scores[k-1]

print(cutoff)
