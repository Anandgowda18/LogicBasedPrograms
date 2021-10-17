'''An e-commerce company plans to give their customers a special discount for the Christmas, they are planning to offer a flat discount. The discount value is calculated as the sum of all prime digits in the total bill amount.
Write an algorithm to find the discount value for the given total bill amount.

Input Format

the input consists of an integer order value representing the total bill amount

Constraints

no conditions

Output Format

print an integer representing discount value for the given total bill amount.

Sample Input 0

123
Sample Output 0

5
Sample Input 1

4589
Sample Output 1

5
Sample Input 2

1700
Sample Output 2

7'''

#solution

def discount(num):
    total_discount = 0
    prime_int = ['2','3','5','7']
    for i in str(num):
        if i in prime_int:
            total_discount = total_discount + int(i)
    return total_discount
print(discount(int(input())))