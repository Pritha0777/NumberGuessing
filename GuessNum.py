#Code to create a number guessing game
import random
import time

def intro():
    print("Please enter your name")
    name = input()
    print(f"{name}, we are going to play a game. I am thinking of a number between 1 and 200")
    time.sleep(0.5)
    print("Go ahead. Guess!")
    return name

def pick(name, number):
    guesses_taken = 0
    while guesses_taken <6:
        time.sleep(0.25)
        enter = input("Guess: ")
        try:
            guess = int(enter)
            if 1<= guess <= 200:
                guesses_taken +=1
                if guess == number:
                    break
                elif guess < number:
                    print("The guess is too low")
                else:
                    print("The guess is too high")
                if guesses_taken < 6: 
                    time.sleep(0.5)
                    print("Try Again")
            else:
                print("The number isn't in the range!")
                time.sleep(0.25)
                print("Please enter a number between 1 and 200")

        except ValueError:
            print(f"I don't think that '{enter}'is a number. Sorry")
    
    if guess == number:
        print(f"Good Job, {name}! You guessed the number in {guesses_taken} guesses!")
    else:
        print(f"Nope. The number I was thinking was {number}")

        
def main():
    playagain = "yes"
    while playagain.lower() in ["yes","y"]:
        number = random.randint(1,200)
        name = intro()
        pick(name, number)
        print("Do you want to play again?")
        playagain = input()

if __name__ == "__main__":
    main()