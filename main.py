#Example 1
print("Hello Stephen, Here is Leo's home work.")

N = int (input ("Please give me 4-digit number that is even and also does not end with a 0 :"))
#This is to ask user a 4-digit number

if N % 2 == 0:
#This is to check N is an even
    if N % 10 != 0:
    #This is to check N dose not end with 0
        if N <= 9999 :
        #This is to check N is smaller than 4-digit number
            if N >= 1000 :
            #This is to check N is greater than 4-digit number
               print("Thank you")
            else:
                print("This number is too small")
        else:
            print("This number is too big")
    else:
        print("This number is end with a 0")
else:
    print("This number is not a even")
#quit()   #Let us pretent here is a quit()
#And would you mind check my second way to solve this home work?

#Example 2:
print("Hello Stephen, Here is Leo's home work.")

N = int (input ("Please give me 4-digit number that is even and also does not end with a 0 :"))
#This is to ask user a 4-digit number

if N >= 1000 and N <= 9999:#To check 1000<N<9999
   if N %  2!=0:#To check the number is an even end with 0
       print("This number an odd")
   elif N % 10 != 0:
        print("Thank you")# good number
   else:#If N is not even or not end with 0
       print('This number is end with 0')
else:#If N<1000 OR N>9999 have two situation
    if N < 1000:#Situation one
        print("This number is too small")
    else:#Satuation two
        print("This number is too big")
quit()
