def test_solution():
    from patterns.problem_1.solution_1 import sum_two_numbers

    input = 3

    expect_output = 5
    actual_output = sum_two_numbers(a=3, b=3)
    print(actual_output)
    assert expect_output == actual_output
