import random
def get_guess(max_num):
    guess = input(f"Please input a number between 1 and {max_num} (No Spaces, decimals, or commas): ")
    if guess != "":
        for char in guess:
            if not (48 <= ord(char) <= 57): #If input is a number between 0-9
                return -1
        return int(guess)
    return -1
def main():
    guessed = []
    cont = True
    while cont:
        mode = input("Input your difficulty 'E' for easy, 'M' for medium, 'H' for hard: ")
        if mode in ["E","M","H"]:
            cont = False
    if mode == "E":
        max_attempts = 9
        max_num = 100
        print(f"You will have {max_attempts} to guess the number between 1 and {max_num}")
    elif mode == "M":
        max_attempts = 8
        max_num = 200
        print(f"You will have {max_attempts} to guess the number between 1 and {max_num}")
    elif mode == "H":
        max_attempts = 7
        max_num = 500
        print(f"You will have {max_attempts} to guess the number between 1 and {max_num}")
    else:
        return -1
    attempts = 0
    guess = -1
    number = random.randint(1,max_num)
    while guess != number and attempts < max_attempts:
        guess = get_guess(max_num)
        if guess in guessed:
            print("Already guessed!")
        elif (guess == -1):
            print("Not a valid guess")
        elif (guess > max_num or guess < 1):
            print("Very funny, please input a number inside the given range")
        else:
            if(guess > number):
                print(f"Too High, {max_attempts - attempts - 1} left")
                attempts += 1
                guessed.append(guess)
            elif(guess < number):
                print(f"Too Low, {max_attempts - attempts - 1} left")
                guessed.append(guess)
                attempts += 1
    if guess != number:
        print(f"Ran out of guesses! The number was {number}")
    else:
        print(f"Congratulations! You guessed {number} correctly in {attempts + 1} attempts")
if __name__ == "__main__":
    main()