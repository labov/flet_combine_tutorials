#!/bin/bash
printg() {
  printf "\e[32m$1\e[m\n"
}

printg "===  Run __main__.py  ========================== \n"
DIR="$( cd "$( dirname "$0" )" && pwd )"
/usr/bin/python3 $DIR/__main__.py
