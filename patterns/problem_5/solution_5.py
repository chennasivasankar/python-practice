def solution5(n: int):
    for i in range(1, n + 1):
        out_put = str((str(i) + " ") * i)
        print(out_put[:-1])