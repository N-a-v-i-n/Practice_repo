if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())    #This will give list of input data in i.e 2 3 6 6 5
    arr2=set(arr)  # removing duplicates 
    #print(list(arr))  
    max_val=max(arr2)  # finding max value after filter
    arr2.remove(max_val) # removing that max_val from list 
    print(max(arr2)) # printing second max val
    