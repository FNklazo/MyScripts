from random import choice
from main_utils import OpenShop, UserExtras, YouWin, YouDrew, YouLose, GetUser, GetRPS, RPS

def main():
    while True:
        user = GetUser('Rock, Paper, or Scissors?')
        user = GetRPS(user)

        if user in RPS:
            ai = choice(RPS)
  
            game = {'rock':YouDrew, 'paper':YouWin, 'scissors':YouLose} if ai == 'rock' else \
                   {'rock':YouLose, 'paper':YouDrew, 'scissors':YouWin} if ai == 'paper' else \
                   {'rock':YouWin, 'paper':YouLose, 'scissors':YouDrew}
            game[user]()

        elif user in ['shop', 'store']:
            OpenShop()
        
        else:
            UserExtras(user)
        
        
main()

