class Items:
    def __init__(self, itemName, itemPrice):
        self.itemName, self.itemPrice, self.itemStack = itemName, itemPrice, 0

    def __repr__(self):
        return f'(x{self.itemStack}) {self.itemName}'

    def repr(self):
        return self.__repr__(self)

    def find(self, user):
        return bool(self.itemName.casefold().startswith(user))

    def purchase(self, gold, amount):
        global inventory
        
        if (total:=self.itemPrice * amount) <= gold:
            gold -= total
            self.itemStack += amount
            inventory += [self] if self in inventory else []
            print(f"(x{amount}) {self.itemName} succesfully purchased!")
        
        else:
            print(f'Insufficient Funds.{self.itemPrice - gold}G more needed.')
        
        return gold

    def use(self, amount):
        if self is restore_streak and self in inventory:
            message = '\nYour Streak has been restored!'
        
            return bool(self.remove(amount, message))

        elif self is x3_gold and self in inventory:
            message = f'\nYour has multiplier has been increased to {3*amount}!'

            return (3 * amount) if self.remove(amount, message) else 1

        print('\nYou do not own this item.')
        
        return False
    
    def remove(self, amount, message):
        global inventory

        if self.itemStack - amount < 0:
            print('\nYou do not own enough of this item.')
        
            return False

        self.itemStack -= amount
        print(message)
        if self.itemStack == 0:
            inventory.remove(self)
        
        return True


SHOPITEMS = restore_streak, x3_gold = Items('Restore Streak', 2), Items('x3 Gold', 1)
inventory = []


def GetUser(m=''):                      # Its in here to avoid circular import (main_utils <--> shop)
    return (user:= input(f'{m}\n').casefold().strip())

def GetItem(user):
    user = user.split(' ')[1:]
    item, amount = [perk for perk in SHOPITEMS if perk.find(user[0])], int(user[-1]) if user[-1].isnumeric() else 1
    
    return item, amount



def shop_help(user) -> None:
    if user.startswith('-items'):
        [print(f'{item}  >>  {item.itemPrice}G') for item in SHOPITEMS]

    elif user in ['-help', '-buy']:
        print("\nCommands:\n\
                \n-items >>   Shows all avaliable shop items.\
                \n-buy   >>   Purchases an item.             // usage: -buy item [amount]\
                \n-exit  >>   Leaves the shop.")

    else:
        print("\nCommand Prefix is, '-'.")     
        

def shop_purchase(user, gold):
    item, amount = GetItem(user)

    if item:
        gold = item[0].purchase(gold, amount)

    else:
        print(f'This item, {" ".join(iter(user))}, is not avaliable in the shop.')

    return gold


def UserExtras2(user):
    global inventory

    if user in ['e', 'inv']:
        print(inventory or '\nYour inventory is empty.')
    
    

