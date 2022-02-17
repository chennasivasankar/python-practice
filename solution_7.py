def solution7(number: int):
    for i in range(1, number + 1):
        flow_numbers = ""
        for j in range(1, i + 1):
            flow_numbers += str(i * j) + " "
        print(flow_numbers)