# Write a rock, paper, scissors game
# import random module
import random
# define main function that handles all the logic
def main():
    # define variables
    user_wins = 0
    computer_wins = 0
    ties = 0
    # define a variable to control the loop
    play_again = 'y'
    print("Let's play Rock, Paper, Scissors, Lizard and Spock!")
    # loop while the user wants to play again
    while play_again == 'y' or play_again == 'Y':
        # get the user's choice
        user_choice = get_user_choice()
        # get the computer's choice
        computer_choice = get_computer_choice()
        # determine the winner
        winner = determine_winner(user_choice, computer_choice)
        # display the results
        display_results(user_choice, computer_choice, winner)
        # update the appropriate counter
        if winner == 'user':
            user_wins += 1
        elif winner == 'computer':
            computer_wins += 1
        else:
            ties += 1
        # ask the user if they want to play again
        play_again = input('Do you want to play again? (y/n): ')
    # display the final results
    display_final_results(user_wins, computer_wins, ties)

def get_user_choice():
    choices = ['rock', 'paper', 'scissors', 'lizard', 'spock']
    user_choice = input("Please choose one of the following: " + ", ".join(choices) + "\n")
    while user_choice not in choices:
        print("Invalid choice. Please try again.")
        user_choice = input("Please choose one of the following: " + ", ".join(choices) + "\n")
    return user_choice

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors', 'lizard', 'spock']
    return random.choice(choices)

# create function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'tie'
    elif (user_choice == 'rock' and (computer_choice == 'scissors' or computer_choice == 'lizard')) or \
         (user_choice == 'paper' and (computer_choice == 'rock' or computer_choice == 'spock')) or \
         (user_choice == 'scissors' and (computer_choice == 'paper' or computer_choice == 'lizard')) or \
         (user_choice == 'lizard' and (computer_choice == 'spock' or computer_choice == 'paper')) or \
         (user_choice == 'spock' and (computer_choice == 'scissors' or computer_choice == 'rock')):
        return 'user'
    else:
        return 'computer'

# create function to display the results
def display_results(user_choice, computer_choice, winner):
    # display the results
    print('You chose', user_choice)
    print('The computer chose', computer_choice)
    if winner == 'user':
        print('You won!')
    elif winner == 'computer':
        print('The computer won!')
    else:
        print('You tied!')

# create function to display the final results
def display_final_results(user_wins, computer_wins, ties):
    # display the final results
    print('You won', user_wins, 'times')
    print('The computer won', computer_wins, 'times')
    print('You tied', ties, 'times')

if __name__ == '__main__':
    main()
