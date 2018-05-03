# 256-bit-RSA-implementation-with-encryption-and-decryption

256-bit RSA algorithm for encryption and decryption. Encrypt and subsequently decrypt the following text:
“The time has come to talk of many things: of shoes and ships and sealing-wax of cabbages and kings and why the sea is boiling hot and whether pigs have wings.”

Your data block will be of 128-bits. Prepend it with 128 zeroes on the left to make it a 256- bit block. If overall length is not a multiple of 128 bits, append appropriate number of newline characters to it.

Regarding key generation, note the following:
1.	The priority in RSA is to select a particular value of e and choose p and q accordingly. For this assignment, use e = 65537.
2.	Use the PrimeGenerator.py  script to generate values of p and q. Both p and q must satisfy the following conditions:
(a) The two left-most bits of both p and q must be set.
(b) p and q should not be equal.
(c) (p − 1) and (q − 1) should be co-prime to e. Hence, gcd((p − 1), e) and gcd((q − 1), e) should be 1. (hint: use Euclids algorithm to compute the gcd)
If any of the above condition is not satisfied, repeat step:2.
3.	Compute d. You may use the multiplicative inverse function from BitVector class.
4.	After decryption, remove the padded 128 zeroes from each block to make it printable in ASCII form.
 
You should read the input text from a file called message.txt. The encrypted output should be saved to a file called output.txt. The decrypted output should be saved to a file called decrypted.txt. For testing your code, both the output.txt and decrypted.txt files will be used. So ensure that there are no unreadable characters in decrypted.txt
