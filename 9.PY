# 9.	Write a  program to input any character and check whether it is alphabet, digit or special character.
ch = input("Enter your character: ").lower()

if ch >= "a" and ch <= "z":
    print("Character is alphabet")
elif ch >= "0" and ch <= "9":
    print("Character is digit")
else:
    print("Character is special character")
