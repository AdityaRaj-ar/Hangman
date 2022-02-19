import random
from words import list_of_words
def display_hangman(tries):
    stages = [  
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / \\
                   -
                """,
                
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / 
                   -
                """,
                
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |      
                   -
                """,
                
                """
                   --------
                   |      |
                   |      O
                   |     \|
                   |      |
                   |     
                   -
                """,
                
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]

def get_word():
    word = random.choice(list_of_words)
    return word.upper()

def play(word):
    word_completion = "*" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Let's play the game 'Hangman'")
    print("Instructions: ")
    print("1) You have been given a word that is initially hidden.")
    print("2) You can guess a alphabet or a word to find that word.")
    print("3) You have maximum 6 lifes i.e you can commit maximum 6 wrong attempts")
    print("So, Let's start and have fun :)")

    print(display_hangman(tries))
    print(word_completion)
    print("\n")

    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the Letter", guess)
            elif guess not in word:
                print(guess, "is not in the word")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Good job! ", guess, " is in the word!")
                ################
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "*" not in word_completion:
                    guessed = True
                ################
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Not a valid guess.")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("Congratulations! You guessed the word correctly, You Won!")
    else:
        print("Sorry! you ran out of tries. The word was ", word, ". Better luck next time!")

def main():
    word = get_word()
    play(word)
    while input("Do you want to play again?(Yes/No)").upper() == "YES":
        word = get_word()
        play(word)
    print("Hope you enjoyed the game :)")

if __name__ == "__main__":
    main()