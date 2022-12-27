def user_details():
    name = input("enter your name : ")
    age = input("enter your age : ")
    print("please confirm your name is '%s' and you are '%s' years old" %
          (name, age))
    correct = input("please confirm 'y' or 'n' : ")
    if (correct == 'y' or correct == 'Y'):
        print("user_details stored")
    else:
        print("please reEnter")
        return user_details()


user_details()
