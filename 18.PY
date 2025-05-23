# 18.	Write a  program to input marks of five subjects Physics, Chemistry, Biology, Mathematics and Computer. Calculate percentage and grade according to following:
# Percentage >= 90% : Grade A
# Percentage >= 80% : Grade B
# Percentage >= 70% : Grade C
# Percentage >= 60% : Grade D
# Percentage >= 40% : Grade E
# Percentage < 40% : Grade F



p = float(input("Physics marks: "))
c = float(input("Chemistry marks: "))
b = float(input("Biology marks: "))
m = float(input("Mathematics marks: "))
comp = float(input("Computer marks: "))

mark=p+c+b+m+comp
print("total marks is :", mark)
percentage = (p + c + b + m + comp) / 5


if percentage >= 90:
    print("Grade A")
elif percentage >= 80:
    print("Grade B")
elif percentage >= 70:
    print("Grade C")
elif percentage >= 60:
    print("Grade D")
elif percentage >= 40:
    print("Grade E")
else:
    print("Grade F")
