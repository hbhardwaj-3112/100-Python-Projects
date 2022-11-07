# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = round(weight/height**2,2)
bmi_1 = int(round(bmi,0))
if bmi < 18.5:
    print(f'Your BMI is {bmi_1}, you are underweight.')
elif bmi<25:
    print(f'Your BMI is {bmi_1}, you have a normal weight.')
elif bmi<30:
    print(f'Your BMI is {bmi_1}, you are slightly overweight.')
elif bmi<35:
    print(f'Your BMI is {bmi_1}, you are obese.')
else: 
    print(f'Your BMI is {bmi_1}, you clinically obese.')
