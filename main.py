
import sys
import fractions
import math
import decimal




if __name__ == '__main__':




        print(sys.argv[1])
        N=int(sys.argv[1])
        n=int(N*math.log(10, 16))
        Sum_el=0
        for i in range(n):
            Sum_el += fractions.Fraction(47 + 151 * i + 120 * i * i, 16 ** i * (15 + 194 * i + 712 * i * i + 1024 * i * i * i + 512 * i * i * i * i))


        decimal.getcontext().prec = N
        res = decimal.Decimal(Sum_el.numerator)/decimal.Decimal(Sum_el.denominator)

        print(res)