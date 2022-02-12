def solution4(n: int):
    character_nuuber = 64
    for i in range(1, n + 1):
        out_put = (chr(character_nuuber + i) + " ") * i
        print(out_put[:-1])