import random

print("Welcome to Hangman!\n")
animals = [
    "elephant", "zebra", "giraffe", "rhinoceros",
    "crocodile", "chimpanzee", "leopard", "dinosaur", "antelope"
]
word = random.choice(animals)
blanks = ["_"] * len(word)
guessed_letters = []

def game():
    chances = 6
    print("Guess the word:")
    print(" ".join(blanks))
    
    while chances > 0 and "_" in blanks:
        guess = input("Guess a letter: ").lower()
        
        if guess in guessed_letters:
            print("You already guessed that letter. Try another one.")
            continue
        guessed_letters.append(guess)

        if guess in word:
            for index, letter in enumerate(word):
                if letter == guess:
                    blanks[index] = guess
            print("Good guess!")
        else:
            chances -= 1
            print(f"Wrong guess. Chances left: {chances}")

        print(" ".join(blanks))
    
    if "_" not in blanks:
        print("Congratulations! You won")
    else:
        print(f"Time's up... The word was: {word}")

game()
