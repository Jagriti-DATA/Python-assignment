# 16.	Write a  program to check whether the triangle is equilateral, isosceles or scalene triangle.


a = int(input("Enter side 1: "))
b = int(input("Enter side 2: "))
c = int(input("Enter side 3: "))

if a == b and b == c:
    print("Equilateral triangle")
elif a == b or b == c or c == a:
    print("Isosceles triangle")
else:
    print("Scalene triangle")
