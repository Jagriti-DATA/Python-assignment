# 4.	Write a program to check whether a number is divisible by 5 and 11 or not.

num=int(input("enter your number : "))
if(num%5==0 and num%11==0):
    print("number is divisible by 5 and 11")
else:
     print("number is  not divisible by 5 and 11")