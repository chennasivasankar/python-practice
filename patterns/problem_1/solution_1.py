def solution1(n: int):
<<<<<<< HEAD
    double_of_n = n + n - 1
    print((str(n) + " ") * double_of_n)
    first_half = str(n)
    second_half = ""
    appending_numbers = []
    for i in range(1, n):
        b = ""
        the_first_half = " " + str((str(n - (i)) + " ") * (n - (i)))
        the_second_half = (str(n - (i)) + (" ")) * (n - (i + 1))
        b += first_half + the_first_half + the_second_half + second_half + str(n)
        print(b)
        appending_numbers.append(b)
        for descending_order in range(1, n):
            first_half += " " + str(n - i)
            break
        for revers_order in range(1, n):
            second_half = str(n - i) + " " + second_half
            break

    appending_numbers = appending_numbers[:-1]
    for i in range(1, len(appending_numbers) + 1):
        print(appending_numbers[-i])
    if n > 1:
        print((str(n) + " ") * double_of_n)
=======
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
>>>>>>> master
