'''Program to read a number and check whether it is duck number or not.
Hint: A duck number is a number which has zeros present in it, but no zero present in the begining of the number.

Input Format

a number from the user

Constraints

n>=0

Output Format

Yes or No

Sample Input 0

123
Sample Output 0

No
Sample Input 1

140
Sample Output 1

Yes'''

#solution

def duck(num):
    num.lstrip('0')
    if num.count('0')>0:
        return "Yes"
    return "No"

print(duck(input()))
