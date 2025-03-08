import random


#self code

"""
def rock_paper_scissors():
    print("Welcome to Rock, Paper, Scissors!")
    print("Please enter your choice: rock, paper, or scissors.")
    user_choice = input().lower()
    computer_choice = random.choice(["rock", "paper", "scissors"])
    return user_choice, computer_choice


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print("It's a tie!")
        return "It's a tie!"
    elif user_choice == "rock" and computer_choice == "scissors" or user_choice == "paper" and computer_choice == "rock" or user_choice == "scissors" and computer_choice == "paper":
        print("You win!")
        return "You win!"
    else:
        print("You lose!")
        return "You lose!"
        

def play_again():
    print("Do you want to play Rock | Paper | Scissor? (yes or no)")
    ans = input().lower()
    win = 0 
    lose = 0
    tie = 0
    while ans == "yes":
            
            user_choice, computer_choice = rock_paper_scissors()
            score = determine_winner(user_choice, computer_choice)
            print("Do you want to play again? (yes or no)")
            ans = input().lower()

            if score == "You win!":
                win += 1
            elif score == "You lose!":
                lose += 1
            else:
                tie += 1
    else:
        print("Thank you for playing!")
    
    print(f"Your score: {win} wins, {lose} losses, {tie} ties.")



play_again()

"""

