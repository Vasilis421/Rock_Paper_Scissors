def round_winner(player_choice, computer_choice):
    action = {
        "rock": 1,
        "paper": 2,
        "scissors": 3
    }
    if player_choice == computer_choice:  # tie
        print("It's a tie! No points awarded.")
    elif player_choice == action["rock"]:  # user: Rock
        if computer_choice == action["paper"]:  # computer: Paper
            print("Paper covers Rock! Computer wins. 1 point awarded.")
            return False
        elif computer_choice == action["scissors"]:  # computer: Scissors
            print("Rock smashes Scissors! Player wins. 1 point awarded.")
            return True
    elif player_choice == action["paper"]:  # user: Paper
        if computer_choice == action["rock"]:  # computer: Rock
            print("Paper covers Rock! Player wins. 1 point awarded.")
            return True
        elif computer_choice == action["scissors"]:  # computer: Scissors
            print("Scissors cut Paper! Computer wins. 1 point awarded.")
            return False
    elif player_choice == action["scissors"]:  # user: Scissors
        if computer_choice == action["rock"]:  # computer: Rock
            print("Rock smashes Scissors! Computer wins. 1 point awarded.")
            return False
        elif computer_choice == action["paper"]:  # computer: Paper
            print("Scissors cut Paper! Player wins. 1 point awarded.")
            return True
