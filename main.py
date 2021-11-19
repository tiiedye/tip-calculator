# Tip Calculator
print("Welcome to the tip calculator")

bill = input("What was the total bill? $")
tip = input("What percentage tip would you like to give? ")
num_of_people = input("How many people to split the bill? ")

tip_percent = float(tip) / 100
tip_total = float(bill) * tip_percent
bill_total = float(bill) + tip_total
amount_per_person = round(bill_total / int(num_of_people), 2)
amount_per_person_formatted = "{:.2f}".format(amount_per_person)

print(f"Each person should pay ${amount_per_person_formatted}")
