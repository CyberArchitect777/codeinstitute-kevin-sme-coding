import os
import random

HANGMAN_PICS = [
    '''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
========='''
]

DEATH_IMG = '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========='''


def clear_terminal():
  os.system('cls' if os.name == 'nt' else 'clear')


hangman_words = [
    # Movie Titles
    "the godfather",
    "inception",
    "the dark knight",
    "schindlers list",
    "interstellar",
    "gladiator",
    "avengers endgame",
    "the prestige",
    "the departed",
    "whiplash",

    # Games
    "the witcher",
    "dark souls",
    "bloodborne",
    "overwatch",
    "undertale",
    "hollow knight",
    "stardew valley",
    "fortnite",
    "bioshock",
    "celeste",

    # Musicians
    "pink floyd",
    "led zeppelin",
    "radiohead",
    "the beatles",
    "rolling stones",
    "fleetwood mac",
    "coldplay",
    "adele",
    "tchaikovsky"
]

secret_word = random.choice(hangman_words)
guessed_letters = []
lives = 6

while True:
  clear_terminal()
  print(HANGMAN_PICS[len(HANGMAN_PICS) - lives])
  print(f"You've guessed: {guessed_letters}")
  to_display = ""
  for char in secret_word:
    if char == " ":
      to_display += "/ "
    elif char in guessed_letters:
      to_display += f"{char} "
    else:
      to_display += "_ "
  if to_display.count("_") == 0:
    print("You win!")
  else:
    print(to_display)

  user_guess = input("Guess a letter: ").lower()

  if user_guess in guessed_letters:
    print("You already guessed that!")
  else:
    if len(user_guess) == 1:
      guessed_letters.append(user_guess)
      if user_guess in secret_word:
        pass
      else:
        lives -= 1
        if lives == 0:
          print(DEATH_IMG)
          print(f"You died! The word was {secret_word}")
          break
    else:
      if user_guess == secret_word:
        print("You win!")
        break
      else:
        lives -= 1
