from enc_or_dec import *
from util import *
from actions import *




def ask_4_another():
	# ask
	run_again = input('Would you like to save another password? Yes(Y) or No(N)\n ')


	# check input
	# if yes True else False
	if run_again.isalpha() and 'y' in run_again.lower():
		return True

	elif run_again.isalpha() and 'n' in run_again.lower():
		return False

	else:
		# ask again
		return ask_4_another()



# decrypt the file , add the password, and encrypt the file.
# if already decrypted ...add the password, and encrypt the file.
def store_in_bank(psk,key):
	# get content
	f = open('./data/word-bank','rb')
	content = f.read()
	f.close()



	# if file is encrypted, decrypt it , then add psk
	if content.isascii()==False:
		# dec
		enc_n_dec_toggle(key)

	# notify
	print(colors.purple,'inserting into the word-bank now...')


	# append to file
	f = open('./data/word-bank','ab')
	f.write(bytes(f"{psk}\n",encoding='utf-8'))
	f.close()


	# enc file again(secure it)
	enc_n_dec_toggle(key)

	# notfiy
	print(colors.green,'Password is now save in your bank...')


