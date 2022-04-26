import io
import sys

_INPUT = """\
6
2
3
8
2
2
2
12
8
25
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  import math
  a=int(input())
  b=int(input())
  n=int(input())
  print(((n-1)//(a*b//math.gcd(a,b))+1)*a*b//math.gcd(a,b))