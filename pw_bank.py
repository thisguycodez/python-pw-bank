from util import *
from actions import *






print(colors.yellow,'________________________ThisGuyCodez_________')
print(colors.green,'          _________      ')
print(colors.green,'          |_______|      ')
print(colors.green,'          |  \^/  |      ')
print(colors.green,'          |   O   |    Bank For Words')
print(colors.green,'          |  / \  |    ')
print(colors.green,'          |_______|      ')
print(colors.lightred,'_____________________________________________')
print(colors.orange,'Python__Word_Bank_(File Encryption/Decryption)')
print(colors.purple,'_____________________________________________\n\n')



# main menu
def main_menu():


	#asking user for the action 2 take
	ask = input(f"""{colors.yellow}
		SELECT A NUMBER....
		1.) Add a password
		2.) Secure or Unlock the Word Bank{colors.red}
		3.) Quit
		{colors.yellow}
		""") 



	# check input
	if ask.isnumeric():

		if '1' in ask:
			return choice_one(main_menu)
		
		elif '2' in ask:
			return choice_two(main_menu)
		
		elif '3' in ask:
			return False

	# loop the main menu
	return main_menu()



main_menu()