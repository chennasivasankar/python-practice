def floyd_s_triangle(number: int):
    num = 1
    for i in range(0, number):
        count = ""
        for j in range(0, i + 1):
            count = count + str(num) + " "
            num = num + 1
        print(count)
