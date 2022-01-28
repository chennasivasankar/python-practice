def solution1(n: int):
    l = n
    double_of_n = n + n - 1
    print((str(n) + " ") * double_of_n)
    c = ""
    for i in range(1, l):
        b = ""
        b += c + " " + str((str(l - (i)) + " ") * (double_of_n - (2))) + str(l)
        for j in range(1, l):
            c += str(l - i)
            print(c)
            break


def sum_two_numbers(a: int, b: int):
    return a + b
