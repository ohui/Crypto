# Oliver Hui
# Pohlig-Hellman Algorithm in Python

# Inspired mainly by the following links
# https://web.math.rochester.edu/people/faculty/edummit/docs/cryptography_3_discrete_logarithms_in_cryptography.pdf
# https://www.youtube.com/watch?v=BXFNYVmdtJU
# http://www-math.ucdenver.edu/~wcherowi/courses/m5410/phexam.html

from sympy.ntheory import factorint

# Values here were from the following link
# http://www-math.ucdenver.edu/~wcherowi/courses/m5410/phexam.html
alpha = 6
startBeta = 11850
p =  8101

factors=factorint(p-1)  #builds a dict of prime factors of (p-1)
xi = [] # This will hold all the x's 
mods = [] # This will hold the different mods
# Above 2 variables will be shoved into the Chinese Remainder Theorem solver function

def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
 
    for n_i, a_i in zip(n, a):
        p = prod / n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod
 
 
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a / b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

# Above 2 functions were taken from http://rosettacode.org/wiki/Chinese_remainder_theorem


def extended_gcd(aa, bb):
    lastremainder, remainder = abs(aa), abs(bb)
    x, lastx, y, lasty = 0, 1, 1, 0
    while remainder:
        lastremainder, (quotient, remainder) = remainder, divmod(lastremainder, remainder)
        x, lastx = lastx - quotient*x, x
        y, lasty = lasty - quotient*y, y
    return lastremainder, lastx * (-1 if aa < 0 else 1), lasty * (-1 if bb < 0 else 1)

def modinv(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise ValueError
    return x % m

#Above 2 functions were taken from https://rosettacode.org/wiki/Modular_inverse#Python




def buildAlphaKnowns(q):
    # find all values of alpha^(k*(p-1)/q) mod p for k = 0,...,max-1
    # returns an array
    result = []
    for i in range(q):
        result.append(int((alpha**(i*(p-1)/q))%p))
    return result
    
def findXi(q,iMax, knowns):
    # Find the Di's which we will sum up later
    # We loop and calcualte bi^(p-1)/q(i+1)
    xi = []
    inverse = modinv(alpha,p)

    #initialize
    b = startBeta
    bi = (b**((p-1)/q))%p
    
    for i in range(iMax):    
        if i != 0:
            # Update 
            expon = xi[i-1] * q**(i-1)
            b = (b*inverse**(expon))%p
            bi = (b**((p-1)/q**(i+1)))%p
        xi.append(knowns.index(bi))
        
    return xi

# Main program starts here

for k, v in factors.items():
    mods.append(k**v)
    
    alphaKnowns= buildAlphaKnowns(k) # Build these values that we will reference later
    
    qxi = findXi(k,v, alphaKnowns) # For each prime factor, get their x's
    
    accumX = 0 
    
    for i in range(len(qxi)):
        accumX += qxi[i]*k**i
    
    xi.append(accumX%(k**v))


print xi
print mods
# Output is 
# [1, 47, 14]
# [4, 81, 25]

# This means
# x = 1 mod 47
# x = 47 mod 81
# x = 14 mod 25
# We now use the Chinese Remainder Theorem solver function to solve for x

answer = chinese_remainder(mods, xi)

print "\nx is " + str(answer)
# X should be 6689
# as stated on the website
# http://www-math.ucdenver.edu/~wcherowi/courses/m5410/phexam.html

