def solution8(number: int):
    flow_number = "1"
    adding_in_list = []
    for i in range(1, number+1):
            for j in range(1, i+1):
                if (j % 3) >= 1 and (j % 2) == 0:
                    flow_number = str(j) + "  " + flow_number
                    break
            sum_number = 1
            for k in flow_number:
                if k == " ":
                    pass
                else:
                    sum_number = (sum_number * int(k))
            adding_in_list.append((sum_number))
    solution = ""
    for i in adding_in_list:
        solution = str(i) + "  " + solution
        print(solution)