# 7.	Write a program to check whether a character is alphabet or not.

ch=input("enter character : ")
if ('a' <= ch  and ch <= 'z') or ('A' <= ch and ch <= 'Z'):
    print("Alphabet")
else:
    print("Not an alphabet")