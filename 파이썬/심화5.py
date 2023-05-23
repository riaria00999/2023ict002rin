import math
C = int(input())

for _ in range(C):
    score = list(map(int, input().split()))
    N = score[0]
    scores = score[1:]
    
    average = sum(scores) / N
    average2 = sum(score > average for score in scores)
    percentage = (average2 / N) * 100
    
    print("{:.3f}%".format(math.ceil(percentage)))
