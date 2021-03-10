# * "open" is a function that is used to open a file in a certain mode. Takes 2 args ('filepath',mode). 
# * This is looping through each value within them
# * This can cause you to execute code to manipulate each value within them
# * More on file handling here (https://www.w3schools.com/python/python_file_handling.asp)


# open file in read mode..returns error if file is not there
f = open('./data/filename.txt','r')
# useful to save into a var for better/easier manipulation
content = f.read()
# when captured in var close file
f.close()

# open file in write mode..creates file if file is not there
f = open('./data/filename.txt','w')
# you can now write directly in file
f.write('some text an stuff')
# when text overwrites file close file
f.close()

# open file in append mode..creates file if file is not there
f = open('./data/filename.txt','a')
# you can now add text directly in file
f.write('some more text an stuff\n')
# when text is added close file
f.close()

# open file in just create it..returns error if file is already there
open('./data/filename.txt','x')
