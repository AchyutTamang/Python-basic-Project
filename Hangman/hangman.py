import random

# List of words for the game
words = ["python", "hangman", "challenge", "programming", "developer", "openai"]

def choose_word():
    return random.choice(words)

def display_hangman(tries):
    stages = [
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        =========
        """,
        """
           -----
           |   |
               |
               |
               |
               |
        =========
        """
    ]
    return stages[tries]

def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    tries = 6
    
    print("Let's play Hangman!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    
    while not guessed and tries > 0:
        guess = input("Please guess a letter: ").lower()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Good job,", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                for i, letter in enumerate(word):
                    if letter == guess:
                        word_as_list[i] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        else:
            print("Not a valid guess.")
        
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    
    if guessed:
        print("Congratulations, you guessed the word! You win!")
    else:
        print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time!")

def main():
    word = choose_word()
    play(word)
    while input("Play Again? (Y/N) ").upper() == "Y":
        word = choose_word()
        play(word)

if __name__ == "__main__":
    main()
