# Day 2 project code goes here

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
#(bill * (1+tip/100))/people

total_tip=round(((bill * (tip/100) ) + bill) / people , 2)
#pay=total_tip/people
print(total_tip)