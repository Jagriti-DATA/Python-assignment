# 20.	Write a  program to input electricity unit charges and calculate total electricity bill according to the given condition:
# For first 50 units Rs. 0.50/unit
# For next 100 units Rs. 0.75/unit
# For next 100 units Rs. 1.20/unit
# For unit above 250 Rs. 1.50/unit
# An additional surcharge of 20% is added to the bill


units = float(input("Enter electricity units: "))


bill = 0
if units <= 50:
    bill = units * 0.50
elif units <= 150:
    bill = 50 * 0.50
    remaining = units - 50
    bill = bill + remaining * 0.75
elif units <= 250:
    bill = 50 * 0.50         
    bill = bill + 100 * 0.75 
    remaining = units - 150
    bill = bill + remaining * 1.20
else:
    bill = 50 * 0.50         
    bill = bill + 100 * 0.75 
    bill = bill + 100 * 1.20 
    remaining = units - 250
    bill = bill + remaining * 1.50

surcharge = bill * 0.20
total = bill + surcharge
print("Total Electricity Bill = ₹", total)

