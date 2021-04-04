def winning_score():
    while True:
        try:
            winning_score = int(input("\nHow many points should "
                            "declare the winner? "))
        except ValueError:
            print("\nInvalid input type. Enter a positive number.")
            continue
        else:
            if winning_score <= 0:
                print("\nInvalid input value. Enter a positive number.")
                continue
            return winning_score
