def diamond_pattern_of_star(number: int):
    middle_spaces = number
    print(" " * number + " *")
    for i in range(number - 1):
        the_pattern = " " * (middle_spaces - i) + "*" + "  " * i + " *"
        print(the_pattern)
    for j in range(3, number + 1):
        revers_pattern = " " * j + "*" + "  " * (middle_spaces - j) + " *"
        print(revers_pattern)
    print(" " * number + " *")