'''Given an integer, create a function that returns the next prime. If the number is prime, return the number itself.

Input Format

a number

Constraints

no

Output Format

prime number

Sample Input 0

12
Sample Output 0

13
Sample Input 1

24
Sample Output 1

29'''

#solution

def prime(num):
    for i in range(2,num):
        if num % i == 0:
          return False
    return True

num = int(input())
while True:
    if prime(num):
        print(num)
        break
    num = num + 1