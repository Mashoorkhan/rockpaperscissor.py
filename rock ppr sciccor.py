import random
users_choice = int(input("0 for rock, 1 for paper, 2 for scissors: "))
computer_choice = random.randint(0, 2)
print("computer chose:", computer_choice)
if computer_choice == users_choice:
    print("It's a draw")
elif computer_choice == 0 and users_choice == 2 or \
     computer_choice == 1 and users_choice == 0 or \
     computer_choice == 2 and users_choice == 1:
    print("Computer won")
else:
    print("You won")

