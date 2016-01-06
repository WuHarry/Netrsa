# 快速幂取模
"""
e = e0*(2^0) + e1*(2^1) + e2*(2^2) + ... + en * (2^n)

b^e = b^(e0*(2^0) + e1*(2^1) + e2*(2^2) + ... + en * (2^n))
    = b^(e0*(2^0)) * b^(e1*(2^1)) * b^(e2*(2^2)) * ... * b^(en*(2^n))

b^e mod m = ((b^(e0*(2^0)) mod m) * (b^(e1*(2^1)) mod m) * (b^(e2*(2^2)) mod m) * ... * (b^(en*(2^n)) mod m) mod m
"""


def fastExpMod(b, e, m):
    result = 1
    while e != 0:
        if (int(e) & 1) == 1:
            # ei=1,then mul
            result = (result * b) % m
        e = int(e) >> 1
        # b, b^2, b^4, ... , b^(2^n)
        b = (b * b) % m
    return result