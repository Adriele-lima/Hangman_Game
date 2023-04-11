import random
from words import word_list

def play_game():
    """
    Create the game adding print statements with instructions,
    number of tries, animated hangman and also disply the
    letters in the word as you add it correctly.
    Creates the input area for player to guess a letter.
    Check if the guess letter is correct or not.
    """
    
    print('*' * 35)
    print("Welcome to Hangman game!")
    print('*' * 35)
    print("Your goal is to guess the word.")
    print("You'll have to try one letter or word at a time.")
    print("If you miss, one part of your body will be hanged.")
    print("One tip!! It's related to food.")
    print("Good Luck!")
    print('*' * 35)

def get_word():
    """
    It will chose a random word from list of words and change
    it to uppercase.
    """
    word = random.choice(word_list)
    return word.upper()

def check_guesses(word):
    """
    It will create the necessary variables for the game and 
    check all the conditions to check if word/letter is correct.
    """
    word_board = "_" * len(word)
    guessed_letters = []
    guessed_words = []
    tries = 7

    while tries > 0:
        
        #makes the word uppercase.
        guess = input("Enter a letter or a word:\n").upper() 

        #Check if letter is on alphabet.
        if len(guess) == 1 and guess.isalpha(): 
            
            #Check if letter is already guessed.
            if guess in guessed_letters: 
                print("You already guessed", guess)

            #Check if letter is not the word and reduce the number of tries.
            elif guess not in word: 
                print(guess, "guess is not in word.")
                tries -= 1
                guessed_letters.append(guess)
                hangman_tries(tries)
                print(word_board)
                print("\nYou only have", tries, "tries")
                print('-' * 35)

                #"You lose" message.
                if tries == 0:
                    print("Correct word was", word)
                    player_lose()                

            else:

                #If letter is correct it will be accept.
                print("Well done!", guess, "is in word!") 
                guessed_letters.append(guess)
                word_as_list = list(word_board)
                
                """Create variable word_board that print the letter on the 
                correct possition when displaying the word."""
                indices = [i for i, letter in enumerate(word) if letter == guess]                
                for index in indices: 
                    word_as_list[index] = guess
                word_board = "".join(word_as_list)

                print(word_board)
                print('-' * 35)

                #Check if word is correct. "You won" message is called.
                if "_" not in word_board:
                    player_win()
                    tries = 0


        #Check if word has the same amount of letters and is on alphabet.
        elif len(guess) == len(word) and guess.isalpha():

            #Checks if word is already guessed.
            if guess in guessed_words:
                print("You already guessed the word", guess)

            #Check if word is not the word and reduce the number of tries.
            elif guess != word:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)

                #"You lose" message.
                if tries == 0:
                    print("Correct word was", word)
                    player_lose()

                hangman_tries(tries)
                print(word_board)
                print('-' * 35)

            #Check if word is correct. "You won" message is called.
            else:
                player_win()
                tries = 0
        
        #Check if word/letter guessed is invalid.
        else:
            print("Not a valid guess.")
            print('-' * 35)

def hangman_tries(tries):
    """
     Create a hangman caricature of each stage.
    """

    print("  _______     ")
    print(" |/      |    ")

    if (tries == 6):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if (tries == 5):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if (tries == 4):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if (tries == 3):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if (tries == 2):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if (tries == 1):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (tries == 0):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def player_win():
    """
    Create a win caricature.
    """
    print("Congrats, you guessed the word! You win!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def player_lose():
    """
    Create a lose caricature.
    """
    print("Sorry, you ran out of tries. Maybe next time!")
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def main():
    """
    Calls all the functions.
    """
    play_game()
    word = get_word()
    check_guesses(word)

    while input("Play Again? (Y/N) \n").upper() == "Y":
        play_game()
        word = get_word()
        check_guesses(word)

main()