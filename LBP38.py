'''A company launched a new text editor that allows users to enter english letters, numbers and white spaces only. If a user attempts to enter any other type of characters, it is counted as miss. Given a String text, write an algorithm to help the developer detect the number of misses by a given user in the given input.

Input Format

String

Constraints

non-empty string

Output Format

number of misses

Sample Input 0

aa a234bc@ sa% hasgd^
Sample Output 0

3
Sample Input 1

g@@d morning#
Sample Output 1

3'''

#solution

miss = 0
for i in input():
    if not(i.isalnum() or i == ' '):
        miss = miss + 1
print(miss)