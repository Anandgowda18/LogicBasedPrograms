'''Write a program to check whether the given number is prime number or not. A number is said to prime if it is having only two factors. i.e. 1 and number itself.

Input Format

a number from the use

Constraints

n>1

Output Format

true or false

Sample Input 0

2
Sample Output 0

true
Sample Input 1

3
Sample Output 1

true'''

#solution

def print_num(num):
    if num > 1:
        for i in range(2,num):
            if num%i == 0:
                return "false"
        return "true"

print(print_num(int(input())))