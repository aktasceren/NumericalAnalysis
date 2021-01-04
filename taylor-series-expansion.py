from sympy import diff, sin, exp
import math
from sympy.abc import *

x, a = symbols("x a")

#derivative of function
def der(expr, n):
    if n > 1:
        return der(diff(expr), n-1)
    return expr

def taylor_expansion(func, process):
    # process -= 1
    TaylorExpansion = func
    f = der(func, 2)
    for i in range(1, process):
        TaylorExpansion += pow(x-a, i)*der(f, i) / math.factorial(i)
    return TaylorExpansion

TaylorExpansion = taylor_expansion(sin(2*a), 5)
#print("Taylor series expension where a = 0: ", TaylorExpansion)

TaylorExpansion = TaylorExpansion.subs([(x, math.pi/4), (a, 0)])
#print("Taylor series expansion for first five terms where x is pi/4 = ", TaylorExpansion)

#real value of sin2x
realValue = sin(2*(math.pi/4))

#Absolute Error
AbsoluteError = abs(realValue- TaylorExpansion)
print("Absolute error: ", AbsoluteError)

#RelativeError

RelativeError = AbsoluteError/realValue
print("Relative Error:", RelativeError)

#Percentage Error
PercentageError = ((realValue - TaylorExpansion) / realValue) * 100
print("Percentage error: % ", PercentageError)