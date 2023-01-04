# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools
s=input()
def count(x):
    return (len(x))
store_ref2=[]

for key,group in itertools.groupby(s,lambda x:x):
    store_ref=(list(group)) 
    store_ref1=count(store_ref)
    key_cnvt=int(key)
    # print(type(store_ref1))
    print((store_ref1,key_cnvt),end=" ")
