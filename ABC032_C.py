import io
import sys

_INPUT = """\
6
7 6
4
3
1
1
2
10
2
6 10
10
10
10
10
0
10
6 9
10
10
10
10
10
10
4 0
1
2
3
4
3 0
2
1
3
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N,K=map(int,input().split())
  S=[int(input()) for _ in range(N)]
  if 0 in S: print(N)
  else:
    l,r=0,0
    k=1
    ans=0
    while l<N:
      while r<N and k*S[r]<=K:
        k*=S[r]
        r+=1
      ans=max(ans,r-l)
      if r==l:
        k*=S[r]
        r+=1
      k//=S[l]
      l+=1
    print(ans)