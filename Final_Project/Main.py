import random
def get_guess(max_num):
    guess = input(f"Please input a number between 0 and {max_num} (No Spaces, decimals, or commas): ")
    if guess != "":
        for char in guess:
            if not (48 <= ord(char) <= 57):
                return -1
        return int(guess)
    return -1

def main():
    mode = input("Input your difficulty 'E' for easy, 'M' for medium, 'H' for hard: ")
    if mode == "E":
        max_attempts = 9
        max_num = 100
    if mode == "M":
        max_attempts = 8
        max_num = 200
    if mode == "H":
        max_attempts = 7
        max_num = 500
    attempts = 0
    guess = -1
    number = random.randint(1,max_num)
    while guess != number or attempts > max_attempts:
        attempts += 1
        guess = get_guess(max_num)
        if (guess == -1):
            print("Not a valid guess")
            attempts -= 1
        elif(guess > number):
            print("Too High")   
        elif(guess < number):
            print("Too Low")
    if attempts > max_attempts:
        print("Ran out of guesses")
    else:
        print(f"Congratulations! You guessed {number} correctly in {attempts} attempts")
if __name__ == "__main__":
    main()