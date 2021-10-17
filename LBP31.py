'''"Secure Assets Private Ltd", a small company that deals with lockers has recently started manufacturing digital locks which can be locked and unlocked using PINs (passwords). You have been asked to work on the module that is expected to generate PINs using three input numbers.

The three given input numbers will always consist of three digits each i.e. each of them will be in the range >=100 and <=999.

Bellow are the rules for generating the PIN.

The PIN should made up of 4 digits.
The unit (ones) position of the PIN should be the least of the units position of the three numbers.
The tens position of the PIN should be the least of the tens position of the three input numbers.
The hundreds position of the PIN should be least of the hundreds position of the three numbers.
The thousands position of the PIN should be the max of all digits in the three input numbers.
Input Format

three numbers

Constraints

all the numbers must be in the range of >=100 and <=999

Output Format

PIN value

Sample Input 0

123
582
175
Sample Output 0

8122
Sample Input 1

190
267
853
Sample Output 1

9150
Sample Input 2

123
456
789
Sample Output 2

9123'''

#solution

n1 = input()
n2 = input()
n3 = input()
hundred = min(n1[0],n2[0],n3[0])
tens = min(n1[1],n2[1],n3[1])
unit = min(n1[2],n2[2],n3[2])
thousand = max(n1[0],n2[0],n3[0],n1[1],n2[1],n3[1],n1[2],n2[2],n3[2])
pin = thousand+hundred+tens+unit
print(pin)