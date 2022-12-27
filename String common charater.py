n=str(input("Enter any word : "))
count = 0
store_ref = []
for i in n:
    count=0
    for j in n:
        if i==j :
            count +=1
            if i==j and count==2:
                store_ref += i

print("after filer : ",store_ref)
print("after removing dulpicate : ", set(store_ref))