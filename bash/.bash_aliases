#!/bin/bash


## Edit Bash Aliases

alias editaliases='vim ~/.bash_aliases'
alias editcmds='vim ~/.bash_commands'



## Directories

amb="You have been teleported."

alias skl="cd /home/fnklazo/Documents/School && echo $amb"
alias scripts="cd /home/fnklazo/Documents/Scripts && echo $amb"
alias usrshare="cd /usr/share && echo $amb"



## Pacman/Yay Shortcuts

alias install='yay -Syu && yay -S'
alias query='yay -Q'
alias search='yay -Ss'
alias update='yay -Syu'
alias orphans='yay -Qdtq'





