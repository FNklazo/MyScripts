from shop import shop
from shop_utils import GetUser, GetItem, UserExtras2, SHOPITEMS


def YouWin():
    global streak, gold, multiplier
    
    print('\nYou Win!')
    streak += 1
    if streak % 3 == 0:
        print(f'\n{multiplier}+ Gold')
        gold += multiplier

def YouDrew():
    print('\nDraw!')

def YouLose():
    global chances, multiplier, streak

    print('\nYou Lose!')
    chances -= 1
    if chances == 0:
        print(f'\nStreak Lost!\n{"Multiplier Lost!" if multiplier > 1 else ""}')
        chances, multiplier, streak = 2, 1, 0


def GetRPS(user):
    user = list({choice if choice.startswith(user) else user for choice in RPS})
    return user[0] if user[0] in RPS else user[-1]


def OpenShop():
    global gold

    gold = shop(gold)


def UserExtras(user):
    global gold

    if user in ['stats', 'gold']:
        print(f'\nYour current streak is: {streak}\nMultiplier: {multiplier}\nYou have {gold} gold.')
    
    elif user == '$g':
        gold += 5
    
    elif user.startswith('use'):
        item, amount = GetItems(user)
        item[0].use(amount) if item else print(f'\nThis item, {"".join(iter(user))} does not exist..')

    else:
        UserExtras2(user)


RPS = 'rock', 'paper', 'scissors'
gold, streak, multiplier, chances = 5, 0, 1, 2

