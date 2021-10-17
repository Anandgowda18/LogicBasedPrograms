'''An e-commerce company plans to give their customers a discount for the newyears holiday. The discount will be calcualted on the basis of the bill amount of the order placed. The discount amount is the sum of all the odd digits in the customers total bill amount. if no odd digits is present in the bill amount, then discount will be zero.

Input Format

the input consists of an integer bill amount, representing the customers total bill amount.

Constraints

print an integer representing the discount for the given total bill amount.

Output Format

n>0

Sample Input 0

2514795
Sample Output 0

27
Sample Input 1

21000
Sample Output 1

1
Sample Input 2

3700
Sample Output 2

10'''

#solution

odd_list = ['1','3','5','7','9']
discount = 0
n = input()
for i in n:
    if i in odd_list:
        discount+=int(i)
print(discount)