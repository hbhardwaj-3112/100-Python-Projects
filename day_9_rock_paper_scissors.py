# Import relevant libraries
import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
#1. Make a list for play and Welcome the user
play = [rock, paper, scissors]
print('Welcome to the game of Rock, Paper, Scissors')

#2. Ask the user for choice
player_choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n'))

#3. Display user choice if they comply
while player_choice <0 or player_choice>2:
    player_choice = int(input('Please chose among the options? Type 0 for Rock, 1 for Paper or 2 for Scissors\n'))
print(f"You chose \n{play[player_choice]}")
#4. Make and print random choice for computer
computer_choice = random.randint(0,2)
print(f"\nComputer chose:\n{play[computer_choice]}")

#5. Determine logic of outcome
outcome = player_choice-computer_choice
if outcome == 0:
    print('Draw')
elif outcome == -1:
    print("You Lose")
else:
    print("You win")