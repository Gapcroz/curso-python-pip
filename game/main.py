import random

options = ("rock", "paper", "scissors")
rounds = 1
computer_wins = 0
user_wins = 0

while True:
  print("*"*10)
  print("ROUND:", rounds)
  print("\n")
  print("USER: ", user_wins)
  print("COMPUTER", computer_wins)
  print("*"*10)

  user_option = input("¿rock, paper or scissors?: ").lower()
  
  if not user_option in options:
    print("try again")
    continue
  
  computer_option = random.choice(options)
  print("user option: ", user_option)
  print("computer option: ", computer_option)
  
  if user_option == computer_option:
    print("¡a tie!, try again")
  elif user_option == "rock":
    if computer_option == "scissors":
      print("rock beat scissors")
      print("¡user win!")
      user_wins += 1
    else:
      print("paper beat rock")
      print("¡computer win!")
      computer_wins += 1
  elif user_option == "paper":
    if computer_option == "rock":
      print("paper beat rock")
      print("¡user win!")
      user_wins += 1
    else:
      print("scissors beat paper")
      print("¡computer win!")
      computer_wins += 1
  elif user_option == "scissors":
    if computer_option == "paper":
      print("scissors beat paper")
      print("¡user win!")
      user_wins += 1
    else:
      print("rock beat scissors")
      print("¡computer win!")
      computer_wins += 1
      
  if computer_wins == 3:
    print("winner is Computer")
    break
  if user_wins == 3:
    print("winner is User")
    break
  
  rounds += 1