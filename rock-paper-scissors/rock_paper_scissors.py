import random

emojis={'r':'🪨','p':'📃','s':'✂️'}
choice=("r","p","s")
while True:
    user_choice=input('rock ,paper, scissors? (r/p/s): ').lower()
    if user_choice not in choice:
     print("Invalid choice")

    computer_choice=random.choice(choice)

    print(f" your chose {emojis[user_choice]}")
    print(f" computer chose {emojis[computer_choice]}")

    if user_choice ==  computer_choice:
      print("It's a draw")

    if (
    (user_choice =="r" and computer_choice=="s") or
    (user_choice=="s" and computer_choice=="p") or
    (user_choice=="p" and computer_choice=="r")):
     print('you win')

    elif(
    (computer_choice=="s" and user_choice=="p") or
    (computer_choice=="p" and user_choice=="s") or
    (computer_choice=="s" and user_choice=="p")):
     print("computer win")


     should_continue=input('continue or not (y/n)').lower()
     if should_continue == "n":
      print("thanks for playing")
      break
