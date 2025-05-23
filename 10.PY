# 10.	Write a program to check whether a character is uppercase or lowercase alphabet.
ch = input("Enter a character: ")

if ch >= "A" and ch <= "Z":
    print("Uppercase")
elif ch >= "a" and ch <= "z":
    print("Lowercase")
else:
    print("Not an alphabet")

