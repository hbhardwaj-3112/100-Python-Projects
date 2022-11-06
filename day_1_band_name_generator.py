import random
num = random.randint(0,1)
#1. Create a greeting for your program.
print('Welcome to the Band Name Generator')
#2. Ask the user for what city they grew up in.
city = input("What's the name of the city you grew up in: ")
#3. Ask the user for the name of their pet.
pet = input("What's your pet's name: ")
name = [city, pet]
#4. Combine the name of their city and pet and show them their band name
print("Your band name could be",name[num-1], name[num])