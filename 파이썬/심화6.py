import math

C = int(input())

for i in range(C):
    inputs = input().split()
    N = int(inputs[0])
    scores = list(map(int, inputs[1:]))
    average = sum(scores) / N

    above_average_count = sum(score > average for score in scores)

    percentage = (above_average_count / N) * 100
    print(f'{percentage:.3f}%')
