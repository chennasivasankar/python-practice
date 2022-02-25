def diamond_shaped_character_pattern_program(number: int):
    character_number = 64
    for i in range(number + 1):
        number_middle_species = ""
        initial_species = " " * (number - i)
        for j in range(1, i + 1):
            number_middle_species = (number_middle_species + " " + str(chr(character_number + j)))
        print(initial_species, number_middle_species)
    the_first_chr_number = 64 + number
    for k in range(number):
        character_number = the_first_chr_number
        new_flow = ""
        initial_species = " " * (k + 1)
        for l in range(1, number - k):
            new_flow += " " + str(chr(character_number + l))
        the_first_chr_number = (character_number + l)
        print(initial_species, new_flow)