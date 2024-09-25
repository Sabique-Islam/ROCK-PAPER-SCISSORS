import random

user_wins = 0
system_wins = 0
draw = 0

options = ["rock", "paper", "scissors"] # 0    1    2

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break # control goes out of while loop

    if user_input not in options:
        print("Avoid typing errors :)")
        continue # brings the control at the starting of while loop


    random_number = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + "...")

    if user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1

    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1

    elif user_input == computer_pick:
        print("It's a draw")
        draw += 1

    else:
        print("You lost!")
        system_wins += 1

if system_wins > user_wins:
    print("You Lost...")
elif user_wins > system_wins:
    print("Congratulations champ...")
elif user_wins == system_wins:
    print("It's a tie...")    

print("Your score :", user_wins)
print("Computer score: ", system_wins)
print("Number of rounds drawn :", draw)
print("Goodbye!")
