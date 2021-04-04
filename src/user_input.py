def get_user_input():
    player_choice = int(input("\nMake your choice: "))
    if player_choice not in [1, 2, 3]:
        print("\nInvalid input value."
              " Type 1 for Rock, 2 for Paper, 3 for Scissors.")
        return False
    return player_choice
