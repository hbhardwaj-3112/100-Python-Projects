# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bill = 0
#1. bill as per size
if size == 'S':
    bill += 15
elif size == 'M':
    bill += 20
else:
    bill += 25
#2. bill as per add_peperoni
if add_pepperoni.lower() == 'y':
    if size.lower() == 's':
        bill += 2
    else:
        bill += 3
#3. bill as per extra_cheese
if extra_cheese.lower() == 'y':
    bill += 1
#4. total_bill
print(f'Your final bill is: ${bill}.')
