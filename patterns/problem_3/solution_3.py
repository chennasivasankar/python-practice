def solution3(number):
    from math import factorial
    for i in range(number):
        number_middle_species = ""
        initial_species = "  " * (number - i)
        for j in range(i + 1):
            number_middle_species = (
                        number_middle_species + "   " + str(factorial(i) // (factorial(j) * factorial(i - j))))
        print(initial_species, number_middle_species)