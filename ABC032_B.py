import io
import sys

_INPUT = """\
6
abcabc
2
aaaaa
1
hello
10
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  s=input()
  k=int(input())
  ans=set()
  for i in range(len(s)-k+1):
    ans.add(s[i:i+k])
  print(len(ans))