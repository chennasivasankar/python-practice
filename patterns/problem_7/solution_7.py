def pyramid_of_horizontal_number_tables(number: int):
    for i in range(1, number + 1):
        flow_numbers = ""
        for j in range(1, i + 1):
            flow_numbers += str(i * j) + " "
        print(flow_numbers)
