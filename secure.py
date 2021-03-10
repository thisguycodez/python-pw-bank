from enc_or_dec import *
from util import *




# prompting
def prompted_toggling(key,main_menu):

	# open the file
	f = open('./data/word-bank','rb')
	# get the content
	content = f.read()
	f.close()






	# - check if its true then its readable
	# within bytes obj else unreadable
	if content.isascii():
 		print(colors.orange,'Your word bank is already decrypted in the "data" folder for you to view',colors.purple)


	 	# ask to encrypt
	 	ask = input('Or do you wish to encrypt the bank file \n Yes(Y) or No(N) ')


	 	# check input...if yes then enc..else main menu
	 	if ask.isalpha() and 'y' in ask.lower():
	 		# enc
	 		enc_n_dec_toggle(key)
	 		print(colors.green,'File Encrypted!')



	# - its encrypted, so decrypt it
	else:
		# decrypt file
		enc_n_dec_toggle(key)

		# notify user
		print(colors.green,'Word Bank is now readable in the "data" folder for you to view')



	return main_menu()







