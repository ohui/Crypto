# Elliptical Curve Equation is y^2 = x^3 + ax + b
# where a and b are integers
# usually mod n 

from fractions import Fraction

INF = "infinity"


########
# Below code from
# https://rosettacode.org/wiki/Modular_inverse#Python

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

##########



class Point:
    """ Point class represents and manipulates x,y coords. """

    def __init__(self, x, y, n):
        """ Create a new point with x and y passed in"""
        self.x = x
        self.y = y
        self.mod_N = n
        
    def checkForInf(self, secondPoint):
        if secondPoint.x == INF:
            return self

    def dot_itself(self, slopeEqtnFunc):
        slope = slopeEqtnFunc(self.x, self.y)
        return self.calcPoint(slope, self.x)
        
    def calcPoint(self, slope, x2):
        n = self.mod_N
        inv_mod = modinv(slope.denominator, n)
        slope = slope.numerator * inv_mod 
        slope =  slope % n 
        x3 = (slope*slope - self.x - x2) % n
        y3 = (slope*(self.x-x3) - self.y) % n
        resPoint = Point(x3, y3, n)
        return resPoint
        
    def add(self, point2):
        self.checkForInf(point2)
        x_diff = point2.x-self.x
        y_diff = point2.y-self.y
        if x_diff == 0:
            #print "\tError: y difference = 0"
            return Point(INF, INF, INF)
        slope = Fraction(y_diff, x_diff)
        resultCoord = self.calcPoint(slope, point2.x)
        return resultCoord

    def subtract(self, point2):
        x_diff = point2.x-self.x
        y_diff = point2.y-self.y
        slope = Fraction(y_diff, x_diff)
        self.calcPoint(slope, point2.x)
    
    def __str__(self):
        if self.x != INF:
            return "(%d, %d)" % (self.x, self.y)
        else:
            return "(infinity, infinity)"
    
    def __eq__(self, other): 
        return self.x == other.x and self.y == other.y and self.mod_N == other.mod_N

    
mod = 17

def derivativeFunc(x,y):
    """Specific derivative to this problem"""
    # y^2 = x^3 + 2x + 2
    # 2yy' = 3x^2 + 2
    # becomes y' = (3x^2 + 2)/2y
    slope = Fraction(3*x*x + 2, 2*y)
    return slope

####################################
print "Given: E: y^2 = x^3 + 2x+ 2 mod 17 and point P = (5,1)"
# Values taken from page 7 of https://koclab.cs.ucsb.edu/teaching/cren/docs/w03/09-ecc.pdf
pE = Point(5,1, mod)       
nextPoint = pE.dot_itself(derivativeFunc)
print "1P = " + str(pE)
print "2P = " + str(nextPoint)
for i in range(19):
    nextPoint = pE.add(nextPoint)
    print "%dP = " % (i+3),
    print str(nextPoint)
    if nextPoint.x == INF:
        break
