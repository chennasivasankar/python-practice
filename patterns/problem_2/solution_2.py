def solution2(n: int):
    print("  " * (n - 1) + str(1))
    for i in range(2, n + 1):
        out_put = ""
        getting_1_middle_numbers = ""
        getting_last_middle_numbers = ""
        initial_speaces = ("  " * (n - i))
        for j in range(1, i):
            getting_1_middle_numbers += " " + str(i + j)
        for j in range(1, i):
            getting_last_middle_numbers = str(i + j) + " " + getting_last_middle_numbers
        if i <= 5:
            out_put += initial_speaces + str(i) + getting_1_middle_numbers + getting_last_middle_numbers[1:] + str(i)
            print(out_put)
        else:
            out_put += initial_speaces + str(i) + getting_1_middle_numbers + getting_last_middle_numbers[2:] + str(i)
            print(out_put)
