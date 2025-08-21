import random
def dice_roll():
    return  random.randint(1, 6)


def coin_toss():
    return random.choice(["heads", "tails"])

while True:
    print('-'*30)
    print('WELCOME TO DICE COIN SIMULATOR\n')
    choice = input('please enter your choice: DICE(d) or COIN(c): ').lower().strip()
    if choice == 'd' or choice == 'c':
        if choice == 'd':
            dice_choice = dice_roll()
            print(f"YOUR DICE CHOICE IS - {dice_choice}")
        if choice == 'c':
            coin_toss = coin_toss().upper()
            print(f"YOUR COIN CHOICE IS - {coin_toss}")
    else:
        print('OOPS,Invalid input please enter a valid choice\n')
