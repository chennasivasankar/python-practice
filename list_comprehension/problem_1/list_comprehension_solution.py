def list_comprehension(the_input):
    the_odd_numbers = [number for number in the_input if number % 2 == 1]
    the_even_numbers = [number for number in the_input if number % 2 == 0]
    return the_odd_numbers, the_even_numbers


the_input = list(map(int, input().strip().split()))
out_put = list_comprehension(the_input)
print(out_put)
