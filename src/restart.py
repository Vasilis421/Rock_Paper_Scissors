def restart():
    prompt = input("Type [y] to play again or any other key to quit. ")
    if prompt.lower() == "y":
        return True
    else:
        return False
