# @file .bashrc
#

# load default bashrc
if [ -f /etc/bashrc ]; then
    . /etc/bashrc
fi

source ~/doc/etc/bashrc

# to fix emacs backspace problem
stty erase "^H"
stty erase "^?"

# GO
export GOROOT=/usr/local/go
export PATH=$GOROOT/bin:$PATH
export GOPATH=$HOME/work/go
export PATH=$GOPATH/bin:$PATH

# MODGO
export MODRPCROOT=/opt/modrpc

if [ $TERM == vt100_ ]; then
    PS1='\033[1m$PS1\033[0m'
fi
#PS1='[\u@\e[0;32m\h\e[m \W]$ '
