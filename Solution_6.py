def solution_6(n: int):
    if n >= 1:
        print("*")
        for i in range(n - 2):
            print("*" + " " * i + "*")
        print("*" * n)
