#1.Welcome the user
print("Welcome to the tip calculator.")
#2.Ask the user for bill amount
amount = float(input("What is the bill amount: $"))
payers = int(input('Number of payers: '))
tip = int(input("What percentage of tip would you like to give?\nPlease put the number not the '%' sign "))
#3. Calulate the individual's bill
bill_per_person = round(amount/payers)
#4.Calculate the final bill
payment = bill_per_person*(1+tip/100)
payment = "{:.2f}".format(payment)
print(f'Each person should pay: ${payment}')