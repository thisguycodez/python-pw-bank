from util import *
from insert import *
from secure import *
from getpass import getpass






# get key
def get_key():
	# ask
	# using getpass to hide entry
	# caution msg about key is 1st

	print(colors.red,"Note: Using different keys can corrupt the file",colors.yellow)
	key = getpass('Please enter in your key if you already have one or enter in a number between 1-255\n')


	# check input
	if key.isnumeric() and int(key) >= 1 and int(key) <= 255:
		return int(key)



	# ask again
	return get_key()




# adding to the file
def choice_one(main_menu):
	
	print(colors.blue)

	# get password
	password = input("What is the password you're adding to the bank?\n  ")

	#check input

	if len([True for x in password if x.isspace()]) > 0:
		print('You need a solid word, no whitespace')

		return choice_one(main_menu)



	# get key
	key = get_key()


	# store psk in the bank
	store_in_bank(password, key)


	# ask for another
	ask = ask_4_another()

	# if we are adding more, restart this def
	if ask:
		return choice_one(main_menu)

	# else main menu
	else:
		return main_menu()





# toggle enc or dec
def choice_two(main_menu):
	# get key
	key = get_key()

	# start prompts function
	prompted_toggling(key, main_menu)
