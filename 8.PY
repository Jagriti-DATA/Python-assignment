# 8.	Write a  program to input any alphabet and check whether it is vowel or consonant.

ch=input("enter alphabet : ").lower()
if(ch=="a" or ch=="e"or ch=="i" or ch=="o" or ch=="u"):
    print("alphabet is vowel")
else:
    print("alphabetr is consonant")
    



#another method using list
li=["a","e","i","o","u","A","E","I","O","U"]
ch = input("Enter an alphabet: ")
if ch in li:
    print("Vowel")
elif (ch not in li):
    print("Consonant")
else:
    print("Invalid input")
