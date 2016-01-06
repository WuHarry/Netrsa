# 扩展欧几里得算法

def extendedGCD(a, b):
    # a*xi + b*yi = ri
    if b == 0:
        return (1, 0, a)
    (x, y, r) = extendedGCD(b, a % b)
    """
    gcd(a, b) = a*xi + b*yi
    gcd(b, a %  b) = b*xi+1 + (a - [a/b]*b)*yi+1
    gcd(a, b) = gcd(b, a %  b)   =>   a*xi + b*yi = a*yi+1 + b*(xi+1 - [a/b]*yi+1)
    xi = yi+1
    yi = xi+1 - [a/b]*yi+1
    """
    tmp = x
    x = y
    y = tmp - (a / b) * y
    return (x, y, r)
