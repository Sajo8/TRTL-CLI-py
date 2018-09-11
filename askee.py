"""
    Copyright (C) 2018 Sajo8

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

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

