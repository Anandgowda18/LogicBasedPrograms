'''The IT company "Soft ComInfo" has decided to transfer its messages through the N/W using new encryption technique. The company has decided to encrypt the data using the non-prime number concept. The message is in the form of a number and the sum of non-prime digits present in the message is used as the encryption key.
Write an algorithm to determine the encryption key.
note: Digit 1 and 0 are considered as a prime number.

Input Format

The input consists of an integer numMsg representing the numeric form of the message.

Constraints

no

Output Format

print an integer representing the encryption key.

Sample Input 0

45673
Sample Output 0

10
Sample Input 1

123
Sample Output 1

0'''

#solution

non_prime = ['0','2','3','5','7']
encrypt = 0
for i in input():
    if not i in non_prime:
        encrypt = encrypt + int(i)
print(encrypt)