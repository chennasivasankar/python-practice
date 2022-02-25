def learn_about_list_comprehensions(the_first_input: int, the_second_input: int, the_third_input: int):
    output_list = []
    n = 3
    for x in range(the_first_input + 1):
        for y in range(the_second_input + 1):
            for z in range(the_third_input + 1):
                output_list.append([x, y, z])

    print("All permutations of [x, y, z] are")
    print(output_list)

    empty_list = []
    for i in range(len(output_list)):
        the_array_output = output_list[i]
        sum_of_three = the_array_output[0] + the_array_output[1] + the_array_output[2]
        if sum_of_three == n:
            pass
        else:
            empty_list.append(output_list[i])
    print("Print an array of the elements that do not sum to n = 3.")
    print(empty_list)
