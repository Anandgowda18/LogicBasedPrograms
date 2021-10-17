'''Write a program to accept a number and check and display whether it is a Niven Number or not.
Niven Number is that a number which is divisible by its sum of digits.

Input Format

a number

Constraints

n>0

Output Format

Yes or No

Sample Input 0

126
Sample Output 0

Yes
Sample Input 1

10
Sample Output 1

Yes'''

#solution

def niven(num):
    summ = 0
    for i in num:
        summ += int(i)
    return "Yes" if int(num) % summ == 0 else "No"
print(niven(input()))