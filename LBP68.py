'''Andy, Ben and Charlotte are playing a board game. the three of them decided to come up with a new scoring system. A player's first initial ("A","B" and "C") denotes that players scoring a signle point. Given a string of capital letters. return an array of the player's score.

Input Format

A string from the user

Constraints

No

Output Format

Score

Sample Input 0

A
Sample Output 0

1 0 0
Sample Input 1

ABC
Sample Output 1

1 1 1'''

#solution

def score(string):
    return (string.lower().count('a'),
string.lower().count('b'),string.lower().count('c'))

input1 = score(input())
print(f"{input1[0]} {input1[1]} {input1[2]}")