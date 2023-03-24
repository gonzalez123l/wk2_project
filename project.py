import random
# myList = ["rock", "paper", "scissors"]
# random.choice(myList)
# print(random.choice(myList))

#imported random for program to return values when playing game
#create a input function so that game will be playable
#allow user to input "rock", "paper", "scissors"
#ask user option to quit after each turn or continue playing "quit" "play again"
# If the player chooses "Rock" and the computer chooses "Paper" display ("You lose"), 
# If the player chooses "Scissors" and the computer chooses "Rock" display ("You Lose")  and 
# If the player chooses "Paper" and the computer chooses "Scissors" then display ("You lose") 

while True:
    user_choice = input("Enter a choice(rock, paper, scissors):")
    choices = ['rock', 'paper', 'scissors']
    bot_choice = random.choice(choices)
    print(f'You chose {user_choice} and the bot chose {bot_choice}')

    if user_choice == bot_choice:
        print(f'You both selected {user_choice} you just tied to a bot, loser! :p')
    elif user_choice == 'rock':
        if bot_choice == 'scissors':
            print(f'Rock beats scissors! You Win! L bot lol')
        else:
            print('Paper beats rock! You lost! You lost to a bot, loser!')
    elif user_choice == 'scissors':
        if bot_choice == 'paper':
            print(f'Rock beats scissors! You Win! L bot lol')
        else:
            print('Paper beats rock! You lost! You lost to a bot, loser!')
    elif user_choice == 'paper':
        if bot_choice == 'rock':
            print(f'Rock beats scissors! You Win! L bot lol')
        else:
            print('Paper beats rock! You lost! You lost to a bot, loser!')
