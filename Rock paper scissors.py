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
print("Welcome to Rock, Paper, Scissors game. ")
game_images=[rock, paper, scissors]
import random
user_choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if user_choice>=3 or user_choice<0:
    print("You have typed invalid number, you lose. ")
else:
 print(game_images[user_choice])
computer_choice=random.randint(0,2)
print(f"Computer chose {computer_choice}")
print(game_images[computer_choice])
if user_choice==0 and computer_choice==1:
    print("You lose the game")
elif computer_choice==user_choice:
    print("Its a draw. Restart the game. ")
elif user_choice==0 and computer_choice==2:
    print("You win the game")
elif user_choice==1 and computer_choice==0:
    print("You win the game")
elif user_choice==1 and computer_choice==2:
    print("You lose the game")
elif user_choice==2 and computer_choice==0:
    print("You lose the game")
elif user_choice==2 and computer_choice==1:
    print("You win the game")
else:
    print("You choose Invalid number.")
