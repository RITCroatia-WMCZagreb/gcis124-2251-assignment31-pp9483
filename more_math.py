'''
@ASSESSME.USERID: pp9483
@ASSESSME.AUTHOR: Patrik Pavlovic
@ASSESSME.DESCRIPTION: Assignment 3.1
@ASSESSME.ANALYZE: YES
'''
import math

def fact(num):
    num=int(num)
    if num <= 0:
        return 0
    else:
        return math.factorial(num)

def root(num):
   num = int(num)
   if num <= 0:
       return 0
   else:
       return math.sqrt(num)
   

def trunk(num):
   num = int(num)
   if num <= 0:
       return 0
   else:
       return math.trunc(num)
       
    

def main():
   num = input("Enter a numeric value: ")
   print(num,"factorial =",fact(num))
   num1 = float(input("Enter a numeric value: "))
   print("The square root of",num1,"=",root(num1))
   num2 = float(input("Enter a numeric value: "))
   print(num2,"truncated =",trunk(num2))

   


if __name__ == "__main__":
    main()