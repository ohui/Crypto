Elliptic Curve Cryptography in Python
=======

The Elliptic Curve Cryptography is a newer crypto system that is overall better than RSA cryptography. It's faster and more secure and requires smaller keys to have the same encryption strength than RSA.

For more information check out the following links that helped me as a beginner:<br>
<a href = "https://www.tutorialspoint.com/cryptography/public_key_encryption.htm"> Tutorials point's ECC </a><br>
<a href ="http://arstechnica.com/security/2013/10/a-relatively-easy-to-understand-primer-on-elliptic-curve-cryptography/"> A gentle primer on ECC</a>


## Run-through
<br>
Values were taken from <a href "https://koclab.cs.ucsb.edu/teaching/cren/docs/w03/09-ecc.pdf"> this pdf</a>

```
Given: E: y^2 = x^3 + 2x+ 2 mod 17 and point P = (5,1)
1P = (5, 1)
2P = (6, 3)
3P =  (10, 6)
4P =  (3, 1)
5P =  (9, 16)
6P =  (16, 13)
7P =  (0, 6)
8P =  (13, 7)
9P =  (7, 6)
10P =  (7, 11)
11P =  (13, 10)
12P =  (0, 11)
13P =  (16, 4)
14P =  (9, 1)
15P =  (3, 16)
16P =  (10, 11)
17P =  (6, 14)
18P =  (5, 16)
19P =  (infinity, infinity)
```
