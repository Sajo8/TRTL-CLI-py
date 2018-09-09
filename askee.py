import random

f_contents = None

def values(number):
    global f_contents

    if number == 1:
        f = open('ascii/flyingturtle.txt', 'r')
        f_contents = f.read()
    elif number == 2:
        f = open('ascii/happyturtle.txt', 'r')
        f_contents = f.read()
    elif number == 3:
        f = open('ascii/pineapple.txt', 'r')
        f_contents = f.read()
    elif number == 4:
        f = open('ascii/seaturtle.txt', 'r')
        f_contents = f.read()
    elif number == 5:
        f = open('ascii/snail.txt', 'r')
        f_contents = f.read()
    elif number == 6:
        f = open('ascii/swanson.txt', 'r')
        f_contents = f.read()
    elif number == 7:
        f = open('ascii/TRTL.txt', 'r')
        f_contents = f.read()
    elif number == 8:
        f = open('ascii/turtle.txt', 'r')
        f_contents = f.read()
    elif number == 9:
        f = open('ascii/turtlefighter.txt', 'r')
        f_contents = f.read()
    else:
        f = open('ascii/walker.txt', 'r')
        f_contents = f.read()

    f.close()
    
    return f_contents

