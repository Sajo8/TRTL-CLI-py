import random

f_contents = None

filenames = ['ascii/flyingturtle.txt', 'ascii/happyturtle.txt', 'ascii/pineapple.txt', 'ascii/seaturtle.txt', 'ascii/snail.txt', \
'ascii/swanson.txt', 'ascii/TRTL.txt', 'ascii/turtle.txt', 'ascii/turtlefighter.txt', 'ascii/walker.txt']

def values(number):

    global f_contents
   
    if number >= 0 and number <= len(filenames):

        f = open(filenames[number])
        f_contents = f.read()
        f.close()
        return f_contents

