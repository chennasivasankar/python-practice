def solution_9(number: int):
    character_nuuber = 64
    for i in range(number + 1):
        number_middle_species = ""
        initial_species = " " * (number - i)
        for j in range(1, i + 1):
            number_middle_species = (number_middle_species + " " + str(chr(character_nuuber + j)))
        print(initial_species, number_middle_species)
    the_first_chr_number = 64 + number
    for k in range(number):
        character_nuuber = (the_first_chr_number)
        new_flow = ""
        initial_species = " " * (k + 1)
        for l in range(1, number - k):
            new_flow += " " + str(chr(character_nuuber + l))
        the_first_chr_number = (character_nuuber + l)
        print(initial_species, new_flow)