#hangman game is about the word guessing where the computer randomly sl=elects a word and keeps it hidden, prints in underscore form. the user has to guess each letter and he's given 6 chances







import random

print("----------WELCOME TO HANGMAN GAME--------------\n")

words = ["apple", "banana", "orange", "monkey", "guitar",
         "rocket", "python", "pizza", "spider", "cookie",
         "castle", "dragon", "wizard", "galaxy", "shadow"]

while True:

    guessed_letter = []
    hidden_word = random.choice(words)
    lives = 6

    print("the hidden word is given below")
    for x in hidden_word:
        print("_", end=" ")

    while lives > 0:

        print("\nword : ", end=" ")

        all_letter_guessed = True

        for x in hidden_word:
            if x in guessed_letter:
                print(x, end=" ")
            else:
                print("_", end=" ")
                all_letter_guessed = False

        if all_letter_guessed:
            print("\ncongrats bro! you did it...")
            print("the hidden word is =", hidden_word)
            break

        user_guess = input("\nenter your guess between (a-z) = ").lower()

        if user_guess in guessed_letter:
            print("the letter is already guessed! try another")
            continue

        guessed_letter.append(user_guess)

        if user_guess in hidden_word:
            print("correct guess:", user_guess)

        else:
            print("wrong guess 🤡")
            lives -= 1
            print("remaining lives 😱 =", lives)

    if lives == 0:
        print("\nyou have no choices remaining 🤡🤡")
        print("the word was:", hidden_word)
        print("better luck next time")

    choice = input("\ndo you want to play again (yes/no) = ").lower()

    if choice == "no":
        print("thank you for playing")
        break