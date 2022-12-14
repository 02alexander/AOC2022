#!/bin/sh

while true
do 
    inotifywait -e modify main.py ${1:-inp} 2>/dev/null
    clear
    ./main.py < ${1:-inp}
done