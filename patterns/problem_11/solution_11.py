def solution11(number: int):
    for i in range(1, number + 1):
        empty_string = ""
        for j in range(1, number + 1):
            if j <= i:
                empty_string += str(i) + " "
            else:
                empty_string += str(j) + " "
        print(empty_string)
