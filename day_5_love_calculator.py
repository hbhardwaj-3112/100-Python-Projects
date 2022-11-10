# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

tru = list('true')
love = list('love')
name1 = name1.lower() + name2.lower()
## Alternate method in #
#t = name1.count('t')
#r = name1.count('r')
#u = name1.count('u')
#e = name1.count('e')
#true = t+r+u+e
#l = name1.count('l')
#o = name1.count('o')
#v = name1.count('v')
#e = name1.count('e')
#love =l+o+v+e
#count = int(str(true)+int(love))
name1 = list(name1)
tru_count = 0
luv_count = 0

for w in name1:
    if w in tru:
        tru_count +=1
    if w in love:
        luv_count += 1

count = int(str(tru_count)+str(luv_count))

if count < 10 or count > 90:
    print(f'Your score is {count}, you go together like coke and mentos.')
elif count>=40 and count<=50:
    print(f"Your score is {count}, you are alright together.")
else:
    print(f"Your score is {count}.")

 