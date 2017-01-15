Pohlig-Hellman algorithm implemented in Python
======

The Pohlig-Hellman (sometimes called the Silver–Pohlig–Hellman) algorithm is used to solve the "discrete log problem". This means solving the exponent x in g^x = e (mod n). However this algorithm does not work well with very large numbers.

A multiplicative group means that there is a generator g for a group G such that it's able to generate all numbers { 1, .... , G-1 }. Our multiplicative group is the n from the last paragraph.

For example, 2 is a generator for the group 5 so g = 2, G = 5 ...<br>
```
2^1 = 2 (mod 5)
2^2 = 4 (mod 5)
2^3 = 3 (mod 5)
2^4 = 1 (mod 5)

(and it repeats....)
2^5 = 2 (mod 5)
2^6 = 4 (mod 5)
....
```

As you can see, for exponents 1 to G-1, we are able to generate all numbers between 1 to G - 1.

# Output

```
[1, 47, 14]
[4, 81, 25]

x is 6689
```

as answered at the bottom of <a href ="http://www-math.ucdenver.edu/~wcherowi/courses/m5410/phexam.html"> http://www-math.ucdenver.edu/~wcherowi/courses/m5410/phexam.html</a>
