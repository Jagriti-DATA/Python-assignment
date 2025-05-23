# 2.	Write a  program to find maximum between three numbers.
num1=int(input("enter 1st number : "))
num2=int(input("enter 2nd number : "))
num3=int(input("enter 3rd number : "))
if(num1>num2 and num1>num3):
    print(num1,"is max number")
elif(num2>num1 and num2>num3):
    print(num2,"is max number ")
else:
    print(num3,"is max number")



#another method using max function

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
print("Maximum is", max(a, b, c))
