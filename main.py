# Tip Calculator
print("Welcome to the tip calculator")

bill = input("What was the total bill? $")
tip_percent = input("What percentage tip would you like to give? ")
num_of_people = input("How many people to split the bill? ")

tip = float(tip_percent) / 100
tip_total = float(bill) * tip
bill_total = float(bill) + tip_total
amount_per_person = round(bill_total / int(num_of_people), 2)

print(f"Each person should pay ${amount_per_person}")
