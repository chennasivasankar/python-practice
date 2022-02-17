def solution_10(number: int):
    middle_spaces = number
    print(" " * number + " *")
    for i in range(number - 1):
        the_pattern = " " * (middle_spaces - i) + "*" + "  " * i + " *"
        print(the_pattern)
    for j in range(3, number + 1):
        revers_pattrn = " " * j + "*" + "  " * (middle_spaces - j) + " *"
        print(revers_pattrn)
    print(" " * number + " *")