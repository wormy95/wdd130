import random

def choose_word():
    words = ['apple', 'banana', 'orange', 'kiwi', 'pineapple', 'strawberry', 'watermelon']
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ''.join([letter if letter in guessed_letters else '_' for letter in word])
    print(display)

def get_guess(guessed_letters):
    while True:
        guess = input('Guess a letter: ')
        if len(guess) != 1 or not guess.isalpha():
            print('Invalid guess. Please enter a single letter.')
        elif guess in guessed_letters:
            print('You already guessed that letter. Try again.')
        else:
            return guess

def check_guess(guess, word, guessed_letters, attempts_left):
    if guess in word:
        print('Good guess!')
    else:
        print('Sorry, that letter is not in the word.')
        attempts_left -= 1
    guessed_letters.add(guess)
    return attempts_left

def play_hangman():
    word = choose_word()
    guessed_letters = set()
    attempts_left = 6

    while True:
        display_word(word, guessed_letters)
        guess = get_guess(guessed_letters)
        attempts_left = check_guess(guess, word, guessed_letters, attempts_left)
        
        if all(letter in guessed_letters for letter in word):
            print('Congratulations, you won!')
            break
        
        if attempts_left == 0:
            print('Sorry, you lost. The word was', word)
            break
        
        print('Attempts left:', attempts_left)
        