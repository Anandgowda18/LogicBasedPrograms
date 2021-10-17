'''Lisa always forgets her birthday which is on th 5th July.
So develop a function/method which will be helpful to remember her birthday.
The function/method checkBirthday return an integer 1, if it is her birthday else return 0.
the function/method checkBirthday accepts two arguments.Month, a string representing the month of her birth and day, an integer representing the data of her birthday.

Input Format

month & day

Constraints

no

Output Format

1 or 0

Sample Input 0

july
5
Sample Output 0

1
Sample Input 1

june
5
Sample Output 1

0'''

#solution

def birthday(day,month):
    return 1 if day == 5 and month.lower() == 'july' else 0    
    
month = input()
day = int(input())
print(birthday(day,month))