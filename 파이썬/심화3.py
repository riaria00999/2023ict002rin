N = int(input())
for i in range(1, 2 * N):
    if i <= N:
        A = " " * (N - i)
        B = "*" * (2 * i - 1)
    else:
        A = " " * (i - N)
        B = "*" * (2 * (2 * N - i) - 1)
    print(A + B)
