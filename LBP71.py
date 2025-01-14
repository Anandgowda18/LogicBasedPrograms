'''Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 positive integers. No floats
or non-positive integers will be passed
For example, when an array is passed like [9, 5, 1, 3, 77], the output should be 4.
'''

def sum_two_small_numbers(numbers):
    numbers.sort()
    return numbers[0]+numbers[1]

print(sum_two_small_numbers([9, 5, 1, 3, 77]))