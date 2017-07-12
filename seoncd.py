import math
import random


# define function in python
'''
def say_hello():
    print 'Hello'
    print 'today is Thursday!'

def print_info(text):
    print 'Value is' + text
    

say_hello()
print_info('June us almost over')
print_info('what do you do on 4th of July')
print_info("What's for lunch?")
'''    

def kofi_cal_power(base,power):
    result = 1
    result=base**power
    print result

def cal_power(base,power):
    result = 1
    for i in range(power):
        result = result * base

    print result
     
cal_power(3,2)
cal_power(2,3)

#a= raw_input('Enter base: ')
#b= raw_input('Enter power: ')

#a=int(a)
#b=int(b)

#cal_power(a,b)
#kofi_cal_power(a,b)
#print math.pow(a,b)

print random.randint(1,3)



