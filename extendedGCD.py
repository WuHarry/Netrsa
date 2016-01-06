# 扩展欧几里得算法
"""
  "    gcd(a, b) = a*xi + b*yi\n"
  "    gcd(b, a %  b) = b*xi+1 + (a - [a/b]*b)*yi+1\n"
  "    gcd(a, b) = gcd(b, a %  b)   =>   a*xi + b*yi = a*yi+1 + b*(xi+1 - [a/b]*yi+1)\n"
  "    xi = yi+1\n"
  "    yi = xi+1 - [a/b]*yi+1\n"
"""


def extendedGCD(a, b):
    if b == 0:
        return (1, 0, a)
    else:
        (x, y, g) = extendedGCD(b, a % b)
        return (y, (x - a / b * y), g)
