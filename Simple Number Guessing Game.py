import random

rand =  random.randrange(1,10)

while True:
    num = int(input("enter a number between 1 to 10: "))
    if num == rand:
        print("correct")
        break
    else:
         if num > 10 or num < 1:
            print("out of range")
         else:   
                if num>rand:
                    print("too high")
                else:
                    print("too low")    
           
