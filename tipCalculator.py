print("Welcome to the Tip Calculator!")
total_bill = float(input("How much is the total bill? "))
tip = float(input("How much tip would you like to give ? 10, 15 or 20? "))
number_of_person = int(input("How many people to split the bill? "))
each_person_bill = (total_bill + (tip/100)*total_bill)/number_of_person
each_person_bill = round(each_person_bill,2)
print(f"Amount of bill each person to pay ${each_person_bill}")

