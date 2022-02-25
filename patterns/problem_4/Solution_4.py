def print_half_pyramid_using_alphabets(n: int):
    character_number = 64
    for i in range(1, n + 1):
        out_put = (chr(character_number + i) + " ") * i
        print(out_put[:-1])
