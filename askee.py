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

filenames = ['flyingturtle', 'happyturtle', 'pineapple', 'seaturtle', 'snail', 'swanson', 'trtl', 'turtle', 'turtlefighter', 'walker']

def askee(fileornumber):

	if str(fileornumber).isdigit() and int(fileornumber) < 10: # if it is a number and less than 10

		f = open('ascii/' + filenames[fileornumber] + '.txt') #open corresponding file		
		f_contents = f.read()
		f.close()
		return {'ascii': f_contents} # no need to return file_exists or not because we know the random integer passed will be within bounds

	else:
		try:

			f = open(f'ascii/{fileornumber}.txt') #open file of key with the same name with dir and file type appended to it
			
			f_contents = f.read()
			f.close()
			return {'file_exists': True, 'ascii': f_contents} # return file_exists because input passed may not exist

		except: # file doesnt exist
			return {'file_exists': False}