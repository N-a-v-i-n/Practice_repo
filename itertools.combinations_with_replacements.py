# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement
def sort(o):
  lis=list(o)
  c=0
  temp=""
  sorted=""
  for x in range(0,len(lis)):
    for y in range(len(lis)):
      if (lis[x]<lis[y]):
        temp=lis[x]
        lis[x]=lis[y]
        lis[y]=temp
  return lis

    
  
a=input()
store_ref=""
store_ref1=""
sub_inner=""
sub_inner1=""
x=0
x1=0
while a[x]!=" ":
  store_ref +=a[x]
  x+=1 
  last_stopped_index = x
s=sort(store_ref)
k=int(a[last_stopped_index+1])

temp=list(combinations_with_replacement(s,k))
 
for x in temp:
    inner=x
    if k==2:
      sub_inner=inner[0]
      sub_inner1=inner[1]
      print (sub_inner,sub_inner1,sep="")
    elif k==3:
      sub_inner=inner[0]
      sub_inner1=inner[1]
      sub_inner2=inner[2]
      print (sub_inner,sub_inner1,sub_inner2,sep="")
    elif k==4:
      sub_inner=inner[0]
      sub_inner1=inner[1]
      sub_inner2=inner[2]
      sub_inner3=inner[3]
      print (sub_inner,sub_inner1,sub_inner2,sub_inner3,sep="")
    elif k==5:
      sub_inner=inner[0]
      sub_inner1=inner[1]
      sub_inner2=inner[2]
      sub_inner3=inner[3]
      sub_inner4=inner[4]
      print (sub_inner,sub_inner1,sub_inner2,sub_inner3,sub_inner4,sep="")
    elif k==1:
      sub_inner=inner[0]
      print (sub_inner,sep="")
