import random

def choose_word(): #to  randomly select a word from the list of words
    words = ['apple', 'banana', 'orange', 'grape', 'strawberry', 'pineapple', 'watermelon', 'kiwi']
    return random.choice(words)

def display_word(word, guessed_letters): 
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += '_'
    return display

def hangman():
    word_to_guess = choose_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    print("Try to guess the word.")

    while attempts > 0:
        print("\nAttempts left:", attempts)
        print("Word:", display_word(word_to_guess, guessed_letters))

        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in word_to_guess:
            print("Incorrect guess!")
            attempts -= 1
        else:
            print("Correct guess!")

        if all(letter in guessed_letters for letter in word_to_guess):
            print("Congratulations! You've guessed the word:", word_to_guess)
            break

    if attempts == 0:
        print("Sorry, you've run out of attempts. The word was:", word_to_guess)

if __name__ == "__main__":
    hangman()
