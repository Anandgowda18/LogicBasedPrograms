'''Create a function that tests whether or not an integer is a perfect number. A perfect number is a number that can be written as sum of its factors. (equal to sum of its proper divisors) excluding the number itself.

Input Format

a number from the user

Constraints

n>0

Output Format

true or false

Sample Input 0

6
Sample Output 0

true
Sample Input 1

28
Sample Output 1

true
Sample Input 2

12
Sample Output 2

false
Sample Input 3

97
Sample Output 3

false'''

#solution

num = int(input())
list1 = sum([i for i in range(1,num) if num%i == 0])
if list1 == num:
    print('true')
else:
    print('false')