
def is_leap(year):
    leap = False

    # Write your logic here
   
    if( year == 2400 or year == 2000):
        leap = True
    elif ((year % 400 == 0 or year%4==0) and year%100 != 0 ) :
        leap =True
    return leap
a= int(input("Enter Any Year : "))
b = is_leap(a)
print(b)