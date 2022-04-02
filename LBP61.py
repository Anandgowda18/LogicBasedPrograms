'''You are given coordinates, a string that represents the coordinates of a square of the chessboard. Below is a chessboard for your reference.

Refer LBP61.PNG file for the diagram

Return true if the square is white, and false if the square is black.

The coordinate will always represent a valid chessboard square. The coordinate will always have the letter first, and the number second.

Input Format

coordinates from the user

Constraints

coordinates.length == 2 'a' <= coordinates[0] <= 'h' '1' <= coordinates[1] <= '8'

Output Format

true or false

Sample Input 0

a1
Sample Output 0

false
Sample Input 1

h3
Sample Output 1

true
Sample Input 2

c7
Sample Output 2

false'''

#solution

alpha_value = {'a':1,
              'b':0,
              'c':1,
              'd':0,
              'f':1,
              'g':0,
              'h':0}
x = input()
if (int(alpha_value.get(x[0])) + int(x[1])) % 2:
    print('true ')
else:
    print('false')