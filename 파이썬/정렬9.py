
N = int(input())

words = []
for _ in range(N):
    word = input().strip()
    words.append(word)

words = list(dict.fromkeys(words))
words.sort(key=lambda w: (len(w), w))

for word in words:
    print(word)
