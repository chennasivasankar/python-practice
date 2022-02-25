def pascal_s_triangle(number):
    from math import factorial
    for i in range(number):
        number_middle_species = ""
        initial_species = "  " * (number - i)
        for j in range(i + 1):
            the_facter_numbers = str(factorial(i) // (factorial(j) * factorial(i - j)))
            number_middle_species = number_middle_species + "   " + the_facter_numbers
        print(initial_species, number_middle_species)
