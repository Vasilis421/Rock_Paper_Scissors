import random

from winning_score import winning_score
from user_input import get_user_input
from restart import restart
from round_winner import round_winner

print("Welcome to Rock, Paper, Scissors! Each won round awards 1 point."
      " You have three choices."
      " Type 1 for Rock, 2 for Paper and 3 for Scissors.")

score = [0, 0]  # [player, computer]
choices = {
    1: "Rock",
    2: "Paper",
    3: "Scissors"
}
# Determine the winning score
win_score = winning_score()
while True:
    # Get player and computer choices
    try:  # catching here so I can test exceptions in test_user_input
        player_choice = int(get_user_input())
    except ValueError:
        print("\nInvalid input type."
              " Type 1 for Rock, 2 for Paper, 3 for Scissors.")
        continue
    else:
        if not player_choice:
            continue
    computer_choice = random.choice(range(1, len(choices) + 1))
    print(f"\nPlayer chose {choices[player_choice]}."
          f" Computer chose {choices[computer_choice]}.\n")
    # Check the winner of the round
    result = round_winner(player_choice, computer_choice)
    if result is True:
        score[0] += 1
    elif result is False:
        score[1] += 1
    print(f"\nTotal Score: Player {score[0]} - {score[1]} Computer")
    # Victory - Play Again?
    if score[0] == win_score:
        print("\nVictory is yours!\n")
        if restart():
            player_score, computer_score = [0, 0]
            win_score = winning_score()
        else:
            break
    # Defeat - Play Again?
    elif score[1] == win_score:
        print("\nYou have been defeated!\n")
        if restart():
            score = [0, 0]
            win_score = winning_score()
        else:
            break
