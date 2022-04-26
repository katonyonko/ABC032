import io
import sys

_INPUT = """\
6
3 10
15 9
10 6
6 4
30 499887702
128990795 137274936
575374246 989051853
471048785 85168425
640066776 856699603
819841327 611065509
704171581 22345022
536108301 678298936
119980848 616908153
117241527 28801762
325850062 478675378
623319578 706900574
998395208 738510039
475707585 135746508
863910036 599020879
340559411 738084616
122579234 545330137
696368935 86797589
665665204 592749599
958833732 401229830
371084424 523386474
463433600 5310725
210508742 907821957
685281136 565237085
619500108 730556272
88215377 310581512
558193168 136966252
475268130 132739489
303022740 12425915
122379996 137199296
304092766 23505143
10 2921
981421680 325
515936168 845
17309336 371
788067075 112
104855562 96
494541604 960
32007355 161
772339969 581
55112800 248
98577050 22
10 936447862
854 810169801
691 957981784
294 687140254
333 932608409
832 42367415
642 727293784
139 870916042
101 685539955
853 243593312
369 977358410
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  from collections import defaultdict
  from bisect import bisect_left, bisect_right
  N,W=map(int,input().split())
  b=[list(map(int,input().split())) for _ in range(N)]
  if N<=30:
    b1,b2=b[:N//2],b[N//2:]
    d1,d2=defaultdict(int),defaultdict(int)
    for i in range(1<<len(b1)):
      k,v=sum([b1[j][1] for j in range(len(b1)) if (i>>j)&1==1]),sum([b1[j][0] for j in range(len(b1)) if (i>>j)&1==1])
      d1[k]=max(d1[k],v)
    for i in range(1<<len(b2)):
      k,v=sum([b2[j][1] for j in range(len(b2)) if (i>>j)&1==1]),sum([b2[j][0] for j in range(len(b2)) if (i>>j)&1==1])
      d2[k]=max(d2[k],v)
    d1=[[k,d1[k]] for k in d1]
    d2=[[k,d2[k]] for k in d2]
    d1.sort()
    d2.sort()
    for i in range(len(d1)-1):
      d1[i+1][1]=max(d1[i+1][1],d1[i][1])
    for i in range(len(d2)-1):
      d2[i+1][1]=max(d2[i+1][1],d2[i][1])
    dd1=[d1[i][0] for i in range(len(d1))]
    dd2=[d2[i][0] for i in range(len(d2))]
    ans=0
    for i in range(len(d1)):
      if dd1[i]>W: break
      ans=max(ans,d2[bisect_right(dd2,W-dd1[i])-1][1]+d1[i][1])
  elif max([b[i][1] for i in range(N)])<=1000:
    d=defaultdict(int)
    d[0]=0
    for i in range(N):
      tmp=d.copy()
      for k in d:
        tmp[k+b[i][1]]=max(tmp[k+b[i][1]],d[k]+b[i][0])
      d=tmp
    ans=max([d[k] for k in d if k<=W])
  elif max([b[i][0] for i in range(N)])<=1000:
    inf=10**20
    d=[inf]*(2*10**5+1)
    d[0]=0
    for i in range(N):
      tmp=d.copy()
      for j in range(2*10**5+1):
        if j+b[i][0]<=2*10**5:
          tmp[j+b[i][0]]=min(tmp[j+b[i][0]],d[j]+b[i][1])
      d=tmp
    ans=max([i for i in range(2*10**5+1) if d[i]<=W])
  print(ans)