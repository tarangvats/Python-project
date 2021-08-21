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
import random
rps = [rock,paper,scissors]
user = input("Choose rock,paper or scissor\n")
computer_choice = rps[random.randint(0,2)]


if(user=='rock'):
  print(rock)
  print(f"Computer chose {computer_choice}")
  if(computer_choice==rock):
    print('Draw')
  elif(computer_choice==scissors):
    print("Congratulation, You Won!")
  elif(computer_choice==paper):
    print("Sorry, You lost!")
  else:
    print("Invalid")      

if(user=='paper'):
  print(paper)
  print(f"Computer chose {computer_choice}")
  if(computer_choice==paper):
    print('Draw')
  elif(computer_choice==rock):
    print("Congratulation, You Won!")
  elif(computer_choice==scissors):
    print("Sorry, You lost!")
  else:
    print("Invalid")

if(user=='scissors'):
  print(scissors)
  print(f"Computer chose {computer_choice}")
  if(computer_choice==scissors):
    print('Draw')
  elif(computer_choice==paper):
    print("Congratulation, You Won!")
  elif(computer_choice==rock):
    print("Sorry, You lost!")
  else:
    print("Invalid")
