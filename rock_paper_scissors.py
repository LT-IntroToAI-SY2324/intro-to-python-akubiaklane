# We will write a rock paper scissors game in class - Complete it in this file
import random

def get_choices():
    options = ['rock', 'paper', 'scissors']
    player_choice = input("rock, paper, scissors: ")
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}

    return choices

    return 

def check_winner(player, computer):
    print(f"You chose {player}, computer chose {computer}")
    if player == computer:
        return "It's a tie"
    elif player == "rock":
        if computer == "scissors":
            return "rock smashes scissors. You win!"
        else:
            return "paper covers rock. You lose."



#choices = get_choices()
#print(choices)
result = check_winner(choices{"player"}, choices{"computer"})
print(result)