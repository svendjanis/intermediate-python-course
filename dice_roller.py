import random

def main():

  dice_rolls = int(input('How many dice would you like to roll? '))
  dice_size = int(input('How many sides are the dice? '))
  batman_sum = 0
  joker_sum = 0

  for i in range(0, dice_rolls):
    roll = random.randint(1, dice_size)
    if i < dice_rolls / 2:
      name = 'Batman'
      batman_sum += roll
    else:
      name = 'Joker'
      joker_sum+= roll
    print(f'{name} rolled a {roll}')
  print(f'Batman rolled {batman_sum}, Joker rolled {joker_sum}')


if __name__== "__main__":
  main()