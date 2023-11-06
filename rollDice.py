import random


def roll_dice(amount: int = 2) -> list[int]:
    if amount <= 0:
        raise ValueError

    rolls: list[int] = []
    for i in range(amount):
        dice = random.randint(1, 6)
        rolls.append(dice)

    return rolls

def main():
  while True:
      user_input: str = input('Enter the number of dice you want to roll: ')
      try:
        if user_input.lower() == 'exit':
          print('Thanks for playing!')
          break
        print(*roll_dice(int(user_input)), sep= ', ')
      except ValueError:
         print('Enter a valid number!!')
        
if __name__ == '__main__':
   main()
