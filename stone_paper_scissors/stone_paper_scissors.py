# STONE PAPER SCISSOR GAME 

import random

#moves and Sccores
moves = ["stone", "paper", "scissor"]
user_score = 0
comp_score = 0

#loop
while True:
    user_move = input("\nEnter Your move (stone, paper, scissor) or 'exit' to quit: ").lower()

    #exit statement
    if user_move == "exit":
        print("\nFinal Score:")
        print(f"You: {user_score} | Computer: {comp_score}")
        print("Thanks for playing!")
        break

    #Invalid choice

    if user_move not in moves:
        print("Invalid move.")
        continue

    #Computer's move
    comp_move = random.choice(moves)
    print(f"Computer choose: {comp_move}")

    #Winner checker
    if user_move == comp_move:
        print("It's a tie!")
    elif (user_move == "stone" and comp_move == "paper"):
        print("You lost. Try again!")
        comp_score += 1
    elif (user_move == "scissor" and comp_move == "stone"):
        print("You lost. try again!")
        comp_score += 1
    elif (user_move == "paper" and comp_move == "scissor"):
        print(f"\033[31mYou lost. Try again!\033[0m")
        comp_score += 1
    else:
        print("\033[1;32mYou won!\033[0m")
        user_score += 1

    #Display current score
    print(f"Score - You: {user_score} | Computer: {comp_score}")