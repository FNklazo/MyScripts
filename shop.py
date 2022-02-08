from shop_utils import GetUser, shop_help, shop_purchase

def shop(gold):
    print(f"\nWelcome to the Booster Store.\
            \nCommand Prefix is '-', use '-help' for more information.\
            \nYou have {gold} gold.")

    while True:
        if (user:= GetUser()).startswith('-buy') and user != '-buy':
            gold = shop_purchase(user, gold)
        
        elif user == '-exit':
            break
        
        else:
            shop_help(user)
    
    return gold
