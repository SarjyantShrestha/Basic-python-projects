from random import randint

# Number Guessing Game

lower_number, higher_number = 1, 10
random_number = randint(lower_number, higher_number)
tries = 3
print(f'Enter a number from {lower_number} to {higher_number}:')

while True:
  try:
    user_input: int = int(input('Guess: '))
  except ValueError as e:
    print('Enter a valid number.')
    continue

  if user_input < random_number:
    print('The \"number\" is higher')
  elif user_input > random_number:
    print('The \"number\" is lower')
  else:
    print('You Guessed it!')
    break

  tries -= 1
  if tries == 0:
    print('L')
    exit()
  else:
      print(f'you have {tries} trie(s) left.')