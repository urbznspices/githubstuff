# Homework 8
# Arel Urbanozo
# EGR 101
# 11/15/2023

import random

weapons = ("rock", "paper", "scissors")  # tuple of weapons

count = 0  # number of games played
playerStats = {"wins": 0, "losses": 0, "ties": 0}  # dictionary of player stats

while True:  # loop until user quits
    userWeapon = input(  # ask user for weapon
        "Choose your weapon: rock, paper, or scissors. Or type 'quit' to quit:\n").lower()
    computerWeapon = random.choice(weapons)  # computer chooses random weapon
    if userWeapon == "quit":  # if user quits, print stats and break loop
        print(  # print stats
            f"Thanks for playing! You played {count} games, won {playerStats['wins']} games, lost {playerStats['losses']} games, and tied {playerStats['ties']} games.")
        break  # break loop
    elif userWeapon not in weapons:  # if user chooses invalid weapon, print error
        userWeapon = print(  # print error
            "Invalid weapon. Please choose rock, paper, or scissors.")
    else:  # if user chooses valid weapon, play game

        print(f"The game has begun")  # print game start

        if userWeapon == computerWeapon:  # if user and computer choose same weapon, tie
            print(  # print tie
                f"You chose {userWeapon} and the computer chose {computerWeapon}. It's a tie!")
            playerStats["ties"] += 1  # add 1 to tie count
            count += 1  # add 1 to game count
        elif userWeapon == "rock" and computerWeapon == "scissors":  # if user beats computer with rock
            print(  # print win
                f"You chose {userWeapon} and the computer chose {computerWeapon}. You win!")
            playerStats["wins"] += 1  # add 1 to win count
            count += 1  # add 1 to game count
        elif userWeapon == "paper" and computerWeapon == "rock":  # if user beats computer with paper
            print(  # print win
                f"You chose {userWeapon} and the computer chose {computerWeapon}. You win!")
            playerStats["wins"] += 1  # add 1 to win count
            count += 1  # add 1 to game count
        elif userWeapon == "scissors" and computerWeapon == "paper":  # if user beats computer with scissors
            print(  # print win
                f"You chose {userWeapon} and the computer chose {computerWeapon}. You win!")
            playerStats["wins"] += 1  # add 1 to win count
            count += 1  # add 1 to game count
        elif userWeapon == "rock" and computerWeapon == "paper":  # if computer beats user with paper
            print(  # print loss
                f"You chose {userWeapon} and the computer chose {computerWeapon}. You lose!")
            playerStats["losses"] += 1  # add 1 to loss count
            count += 1  # add 1 to game count
        elif userWeapon == "paper" and computerWeapon == "scissors":  # if computer beats user with scissors
            print(  # print loss
                f"You chose {userWeapon} and the computer chose {computerWeapon}. You lose!")
            playerStats["losses"] += 1  # add 1 to loss count
            count += 1  # add 1 to game count
        else:  # if computer beats user with rock
            print(  # print loss
                f"You chose {userWeapon} and the computer chose {computerWeapon}. You lose!")
            playerStats["losses"] += 1  # add 1 to loss count
            count += 1  # add 1 to game count
