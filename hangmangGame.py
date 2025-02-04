from wordsList import words
import random


def hangmanArt(wrongGuesses):
    match wrongGuesses:
        case 0:
            return """
            
            
            
            
            """
        case 1:
            return """
                O
                
                
                
            """
        case 2:
            return """
                O
                |
                
                
            """
        case 3:
            return """
                O
               /|
                
                
            """
        case 4:
            return """
                O
               /|\\
                
                
            """
        case 5:
            return """
                O
               /|\\
               / 
                
            """
        case 6:
            return """
                O
               /|\\
               / \\
            """
        case _:
            return ""

def display_man(wrongGuesses):
    print(hangmanArt(wrongGuesses))

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))

def main(): 
    randomWord = random.choice(words).strip()
    wrongGuesses = 0
    hint = ["_"] * len(randomWord)
    guessed_letters = set()
    is_running = True

    print("**************************")
    print("Welcome to Python Hangman!")
    print("**************************")

    while is_running:
        display_man(wrongGuesses)
        display_hint(hint)

        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print(f"{guess} has already been guessed")
            continue
        
        guessed_letters.add(guess)

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input")
            continue

        if guess in randomWord:
            for index in range(len(randomWord)):
                if randomWord[index] == guess:
                    hint[index] = guess
        else:
            wrongGuesses += 1

        if "_" not in hint:
            display_man(wrongGuesses)
            print("YOU WIN!")
            print("The word was: ", end="")
            display_answer(randomWord)
            print("GAME OVER")
            is_running = False
         
        if wrongGuesses >= 6:
            display_man(wrongGuesses)
            print("YOU LOSE!")
            print("The word was: ", end="")
            display_answer(randomWord)
            print("GAME OVER")
            is_running = False

    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again != 'y':
        print("Thanks for playing! Goodbye!")
        is_running = False 
    else:
        main()


if __name__ == "__main__":
    main()