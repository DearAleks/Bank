print("Welcome to the bank *DRAGON'S DEN*, Traveler!")

balance = 0

def get_user_choice(text, valid_choices):
  while True:
    choice = input(text)
    if choice in valid_choices:
      return choice
    print('\nDragon does not understand you!')

def deposit(balance):
  while True:
    try:
      amount = int(input('\nPlease insert the amount of golden coins you want to deposit: '))
      return balance + amount
    except ValueError:
      print('\nDragon does not understand you!')

def withdrowal(balance):
  while True:
    try:
      amount = int(input('\nPlease insert the amount of golden coins you want to withdraw: '))
      if amount > balance:
        print('\nYou do not have enough money in your account!')
      else:
        return balance - amount
    except ValueError:
      print('\nDragon does not understand you!')

def main():
  global balance

  while True:

    user_choice = get_user_choice("\nWhat would you like to do?\n1. Deposit money\n2. Withdraw money\n3. Check balance\n4. Exit\nYour choice is: ", ['1', '2', '3','4'])

    if user_choice == '1':
      balance = deposit(balance)
    elif user_choice == '2':
      balance = withdrowal(balance)
    elif user_choice == '3':
      print(f'\nYour balance is {balance}.')
    elif user_choice == '4':
      print(f'\nThe total amount deposited is {balance} golden coins.\nFarewell, Traveler!')
      break
    else:
      print('\nDragon does not understand what you say. Choose a valid option!')

main()