#!/usr/bin/env python3

import math

def happy_new_year():
    # code goes here!
    counter = 10
    while counter > 0:
        print(counter)
        counter -= 1
    print("Happy New Year!")
        

def square_integers(int_list):
    # code goes here!
    square_list = list()
    for num in int_list:
        square = math.pow(num,2)
        square_list.append(square)
    return square_list    
    
    #option 2 
    #return [i ** 2 for i in int_list]


# def fizzbuzz():
    # code goes here!
    # counter = 1

    # while(counter <= 100):
    #     if(counter % 3 == 0 and counter % 5 == 0):
    #         print("Fizzbuzz")
    #     elif(counter % 3== 0):
    #         print("Fizz")    
    #     elif(counter % 5 == 0):
    #         print("Buzz")
    #     else:
    #         print(counter)
    # counter +=1        


#0r
def fizzbuzz():
    for i in range(1, 101):
        if not i % 15:
            print("FizzBuzz")
        elif not i % 5:
            print("Buzz")
        elif not i % 3:
            print("Fizz")
        else:
            print(i)