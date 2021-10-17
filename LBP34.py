'''Email name should be starts with alphabet and should follw by number or underscore. It should contains either numbers or underscore finally ends with gmail.com only. Then given email id is true otherwise false.

Input Format

email id

Constraints

lowercase alphabet [a-z] followed by underscore or digit and gmail.com

Output Format

true or false

Sample Input 0

abc@gmail.com
Sample Output 0

false
Sample Input 1

abc1@gmail.com
Sample Output 1

true
Sample Input 2

abc_@gmail.com
Sample Output 2

true'''

#solution

import re
if re.fullmatch("[a-z]+[_|0-9]@gmail[.]com",input()):
    print("true")
else:
    print("false")