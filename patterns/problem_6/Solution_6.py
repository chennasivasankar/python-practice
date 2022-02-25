def hollow_triangle_star_pattern(n: int):
    if n >= 1:
        print("*")
        for i in range(n - 2):
            print("*" + " " * i + "*")
        print("*" * n)
