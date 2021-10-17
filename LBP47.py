'''Create a function that determines whether a number is Oddish or Evenish. A number is Oddish if the sum of all of its digits is Odd, and number is Evenish if the sum of all of its digits is even, if a number is Oddish return Oddish else return Evenish.

Input Format

a number

Constraints

n>0

Output Format

Oddish or Evenish

Sample Input 0

43
Sample Output 0

Oddish
Sample Input 1

373
Sample Output 1

Oddish
Sample Input 2

4433
Sample Output 2

Evenish'''

#solution

sum = 0
for i in input():
    sum+=int(i)
if sum%2 == 0:
    print("Evenish")
else:
    print("Oddish")