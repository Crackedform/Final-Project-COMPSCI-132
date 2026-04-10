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
    attempts = 0
    max_num = 100
    number = random.randint(1,max_num)
    guess = -1
    while guess != number:
        attempts += 1
        guess = get_guess(max_num)
        if (guess == -1):
            print("Not a valid guess")
            attempts -= 1
        elif(guess > number):
            print("Too High")   
        elif(guess < number):
            print("Too Low")
    print(f"Congratulations! You guessed {number} correctly in {attempts} attempts")
if __name__ == "__main__":
    main()
        
        
