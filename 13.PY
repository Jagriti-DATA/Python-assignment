# 13.	Write a  program to count total number of notes in given amount.

amount = int(input("Enter amount: "))
count=0
notes = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]

for i in notes:
    if amount>=i:
        count=amount//i
        amount %=i
        print("number of",i,"notes",count)
