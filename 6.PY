# 6.	Write a  program to check whether a year is leap year or not.
year=int(input("enter year : "))
if(year%4==0):
    print(year,"is leap year")
else:
    print(year,"is not a leap year")