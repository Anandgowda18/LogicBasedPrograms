'''Two Strings a and b are called anagrams, if they contain all the same characters in the same frequencies

Input Format

Two Strings

Constraints

No

Output Format

true or false

Sample Input 0

anagram
margana
Sample Output 0

true
Sample Input 1

python
java
Sample Output 1

false'''

#solution

input1 = input()
input2 = input()
dict1 = {i:input1.count(i) for i in input1}
dict2 = {i:input2.count(i) for i in input2}
if dict1 == dict2:
    print('true')
else:
    print('false')