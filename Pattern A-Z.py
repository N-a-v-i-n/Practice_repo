def fun():
    def Aa():
        i=4
        for x in range(5):
            for y in range(5):
                if  (x in range(4) and y in range(i)):
                    print(' ',end='')    
                else:
                    if (x==3 or x==4) and (y==2 or y==3):
                        print(' ',end='')
                    elif (x==4) and (y==1 or y==2 or y==3):
                        print(' ',end='')
                    else:
                        print('*',end='')        
            i-=1
            if(x==4):
                 print(end='')
            else:
                print()

    def Bb():
        i=4
        for x in range(5):
            for y in range(5):
                if  (x in range(0,5,2) and y in range(3,5)):
                    print(' ',end='')  
                elif (x in range(1,4,2)) and (y in range(1,3) or y==4):
                    print(' ',end='')  
                else:
                    print('*',end='')        
            i-=1
            print()

    def Cc():
        i=4
        for x in range(5):
            for y in range(5):
                if  (x==0 or x==4 ) and y==0:
                    print(' ',end='')  
                elif (x in range(1,4,1)) and y in range(1,5):
                    print(' ',end='')  
                else:
                    print('*',end='')        
            i-=1
            print()

    def Dd():
        i=4
        for x in range(5):
            for y in range(5):
                if  (x==0 or x==4) and y in range(3,5):
                    print(' ',end='')  
                elif (x in range(1,4)) and (y in range(1,4)):
                    print(' ',end='')  
                else:
                    print('*',end='')        
            i-=1
            print()

    def Ee():
        i=4
        for x in range(5):
            for y in range(5):
                if  (x==1 or x==3) and y in range(1,5):
                    print(' ',end='')  
                elif x==2 and y==4:
                    print(' ',end='')  
                else:
                    print('*',end='')        
            i-=1
            print()

    def Ff():
        i=4
        for x in range(5):
            for y in range(5):
                if  (x==1 or x==3 or x==4) and y in range(1,5):
                    print(' ',end='')  
                elif x==2 and y==4:
                    print(' ',end='')  
                else:
                    print('*',end='')        
            i-=1
            print()

        
    def Gg():
        i=4
        for x in range(5):
            for y in range(5):
                if  (x==0) and y==0:
                    print(' ',end='')  
                elif (x==1) and (y in range(1,5)):
                    print(' ',end='')  
                elif (x==2) and y==1:
                    print(' ',end='') 
                elif (x==3) and (y in range(1,4,2)):
                    print(' ',end='') 
                elif (x==4) and (y in range(0,4,3)):
                    print(' ',end='') 
                
                else:
                    print('*',end='')        
            i-=1
            print()

    def Hh():
        i=4
        for x in range(5):
            for y in range(5):
                if  (x==0 or x==1 or x==3 or x==4) and y in range(1,4):
                    print(' ',end='')    
                else:
                    print('*',end='')        
            i-=1
            print()

    def Ii():
        i=4
        for x in range(5):
            for y in range(5):
                if  (x==0 or x==4) and (y==0 or y==4):
                    print(' ',end='')  
                elif x in range(1,4) and (y==0 or y==1 or y==3 or y==4):
                    print(' ',end='')  
                else:
                    print('*',end='')        
            i-=1
            print()

    def Jj():
        i=4
        for x in range(5):
            for y in range(5):
                if  x==0 and (y==1 or y==4):
                    print(' ',end='')  
                elif(x==1 or x==2) and (y==0 or y==1 or y==3 or y==4):
                    print(' ',end='')  
                elif x==3 and (y==1 or y==3 or y==4):
                    print(' ',end='')
                elif x==4 and (y==0 or y==3 or y==4):
                    print(" ",end="")
                else:
                    print('*',end='')        
            i-=1
            print()

    def Kk():
        i=4
        for x in range(5):
            for y in range(5):
                if  (x==0 or x==4) and (y==1 or y==4):
                    print(' ',end='')  
                elif (x==1 or x==3) and y in range(2,5):
                    print(' ',end='')  
                elif x==2 and y in range(1,5):
                    print(" ",end="")
                else:
                    print('*',end='')        
            i-=1
            print()

    def Ll():
        i=4
        for x in range(5):
            for y in range(5):
                if  x in range(4) and (y==0 or y==2 or y==3 or y==4):
                    print(' ',end='')  
                elif x==4 and y==0:
                    print(' ',end='')  
                else:
                    print('*',end='')        
            i-=1
            print()

    def Mm():
        i=4
        for x in range(5):
            for y in range(5):
                if  (x==0 or x==3 or x==4) and y in range(1,4):
                    print(' ',end='')  
                elif x==1 and y==2:
                    print(' ',end='')
                elif x==2 and y in range(1,4,2):
                    print(" ",end='')  
                else:
                    print('*',end='')        
            i-=1
            print()

    def Nn():
        i=4
        for x in range(5):
            for y in range(5):
                if  (x==0 or x==4) and y in range(1,4):
                    print(' ',end='')  
                elif x==1 and y in range (2,4):
                    print(' ',end='')  
                elif x==2 and y in range(1,4,2):
                    print(" ",end="")
                elif x==3 and y in range(1,3):
                    print(" ", end="")
                else:
                    print('*',end='')        
            i-=1
            print()

    def Oo():
        i=4
        for x in range(5):
            for y in range(5):
                if  x in range(1,4) and y in range(1,4):
                    print(' ',end='')    
                else:
                    print('*',end='')        
            i-=1
            print()

    def Pp():
        i=4
        for x in range(5):
            for y in range(5):
                if  (x==3 or x==4) and y in range(1,5):
                    print(' ',end='')  
                elif x==1 and y in range(1,4):
                    print(' ',end='')  
                else:
                    print('*',end='')        
            i-=1
            print()

    def Qq():
        i=4
        for x in range(5):
            for y in range(5):
                if  (x==0 or x==3) and y ==4:
                    print(' ',end='')  
                elif x==1 and (y==1 or y==2 or y==4):
                    print(' ',end='')  
                elif x==2 and (y==1 or y==4):
                    print(" ",end="")
                elif x==4 and y in range(4):
                    print(" ",end="")
                else:
                    print('*',end='')        
            i-=1
            print()

    def Rr():
        i=4
        for x in range(5):
            for y in range(5):
                if  x==0  and y==4:
                    print(' ',end='')  
                elif x in range(1,4,2) and( y==1 or y==2 or y==4):
                    print(' ',end='')  
                elif x==2 and (y==1 or y==3 or y==4):
                    print(" ",end="")
                elif x==4 and y in range(1,4):
                    print(" ",end='')
                else:
                    print('*',end='')        
            i-=1
            if(x==4):
                 print(end='')
            else:
                print()

    def Ss():
        i=4
        for x in range(5):
            for y in range(5):
                if  x==1 and y in range(1,5):
                    print(' ',end='')  
                elif x==3 and y in range(4):
                    print(' ',end='')  
                else:
                    print('*',end='')        
            i-=1
            print()

    def Tt():
        i=4
        for x in range(5):
            for y in range(5):
                if  x in range(1,5) and (y in range(1,4,2) or y==0 or y==4):
                    print(' ',end='')    
                else:
                    print('*',end='')        
            i-=1
            print()

    def Uu():
        i=4
        for x in range(5):
            for y in range(5):
                if  x in range(4) and y in range(1,4):
                    print(' ',end='')  
                elif x==4 and (y==4 or y==0):
                    print(' ',end='')  
                else:
                    print('*',end='')        
            i-=1
            print()

    def Vv():
        i=4
        for x in range(5):
            for y in range(5):
                if  x in range(4) and y in range(1,4):
                    print(' ',end='')  
                elif x==4 and (y==4 or y==0 or y==1 or y==3):
                    print(' ',end='')  
                else:
                    print('*',end='')        
            i-=1
            print()

    def Ww():
        i=4
        for x in range(5):
            for y in range(5):
                if  (x==0 or x==1 or x==4) and y in range(1,4):
                    print(' ',end='')  
                elif x==2 and y in range(1,4,2):
                    print(' ',end='')  
                elif x==3 and y==2:
                    print(" ",end="")
                else:
                    print('*',end='')        
            i-=1
            print()

    def Xx():
        i=4
        for x in range(5):
            for y in range(5):
                if  (x==0 or x==4 ) and y in range(1,4):
                    print(' ',end='')  
                elif (x==1 or x==3) and y in range(0,5,2):
                    print(' ',end='')  
                elif(x==2) and (y==0 or y==1 or y==3 or y==4):
                    print(" ",end="")
                else:
                    print('*',end='')        
            i-=1
            print()

    def Yy():
        i=4
        for x in range(5):
            for y in range(5):
                if  x ==0 and y in range(1,4):
                    print(' ',end='')  
                elif x==1 and (y in range(0,5,2)):
                    print(' ',end='')  
                elif (x==2 or x==3 or x==4) and (y==0 or y==1 or y==3 or y==4):
                    print(" ",end="")
                else:
                    print('*',end='')        
            i-=1
            print()
    def Zz():
        i=4
        for x in range(5):
            for y in range(5):
                if  x==1 and (y in range(3) or y==4):
                    print(' ',end='')  
                elif x==2 and (y==0 or y==1 or y==3 or y==4):
                    print(' ',end='') 
                elif x==3 and (y==0 or y==2 or y==3 or y==4):
                    print(" ",end="") 
                else:
                    print('*',end='')        
            i-=1
            print()



    re=[['A',Aa],['B',Bb],['C',Cc],['D',Dd],['E',Ee],['F',Ff],['G',Gg],['H',Hh],["I",Ii],['J',Jj],['K',Kk],["L",Ll],['M',Mm],['N',Nn],['O',Oo],['P',Pp],['Q',Qq],['R',Rr],['S',Ss],['T',Tt],['U',Uu],["V",Vv],["W",Ww],['X',Xx],['Y',Yy],['Z',Zz]]


    word=input("Enter Any Word : ")
    for x in word:
        for y in range(len(re)):
            up=x.upper()
            if up==re[y][0] :
                a=re[y][1]
                a()
                print(end='')
                
                
    else:
        print("Thanks For Trying")



fun()


        



 
