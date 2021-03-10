# Learning Python With Projects (Hang Man) 
> Syntax - Comments, Prints, Variables, Strings, Integers, String Concatenations, Inputs, Comparison operators, Functions, If/Else statements. For loops, List(arrays), getpass, XOR(exclusive or) algorithim, bytearray, bytes, and "open,read,close"(file handling).

> https://youtu.be/oN63xZ99JSw

___

## Tutorial
	    
#### test1.py file

> XOR (exclusive or) algorithim- :
* This simple algorithim compares bytes and returns them(1 or 0)
* if one of them is 1 then return 1
* other than that return 0
* EX: 1 ^ 0 = 1.......1 ^ 1 = 0.....0 ^ 0 = 0

* # more on 'exclusive or'/'xor' algorithim info here (https://en.wikipedia.org/wiki/Exclusive_or)

```python
# open the file in read mode as bytes
	f = open('./data/word-bank','rb')
	# save it to var
	content = f.read()
	f.close()



	# change content into an array of given bytes
	content = bytearray(content)

# loop through content with enumerate to bring iteration along 
	for i,cur_val in enumerate(content):
		# value needs to stay between 1-255(Bytes)

		# ^ sets each (cur_val ^ key) to 1 if one of them is 1, else 0
		# note the byte format of these values are being compared
		content[i] = cur_val ^ key


```

* More on bytearray here (https://www.w3resource.com/python/python-bytes.php)
___

#### test2.py file

> "open,read,close"(file handling) - :
* "open" is a function that is used to open a file in a certain mode. Takes 2 args ('filepath',mode). 
* This is looping through each value within them
* This can cause you to execute code to manipulate each value within them
* More on file handling here (https://www.w3schools.com/python/python_file_handling.asp)


```python
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

```
___


___

> # Password Bank Project - Follow and apply each step.
  

### pw_bank.py
```python
'''
1.) Create functions that encrypts and decrypts the file, taking in an int as the arguement(1-255) named 'key'
	
	a.)open file in read mode as bytes and save the content to a var 

	b.)convert the content into an array of given bytes

	c.)loop through this content and have each line equal the itself XOR the key (cur_val ^ key)

	d.)write the content into the file




2.) Create a function that checks if file is encrypted or not in order to take the right action. Be sure to be interactive with user.

		a.)open file in read mode as bytes and save the content to 	a var 
		
		b.)use '.isascii()' to confirm if file is encrypted or not. If so decrypt it then inform the user, else do the opposite.

		c.)make sure you're able to return to main menu




3.) Create a function that prompts user for the key

		a.)ask for the key. let it be known it needs to be a number and between 1-255. Check input.

		b.)return it as an integer.



4.)Create a function that stores a password in the bank
	
		a.)prompt user for the password and check the input

		b.) make sure file is decrypted before adding in the password

		c.) add the password to the file along with the others(if any)

		d.)encrypt the file when you are finish




5.)Create an Intro and function that lets a user use this program to store passwords securley
		
		a.)Make your intro how ever you want

		b.)ask user for the action they would like to take. can be number select or character select choice.

		c.)for choice 1 or a, they can add to the word bank. For choice 2 or b, they can unlock or secure the word bank. For choice 3 or c, quit game 




'''

```

### Run your app
```bash
python pw_bank.py
```
___


> *CONGRATS YOU JUST PROGRAMMED A Password Bank IN PYTHON*
---
> *SEE HOW FAR YOU CAN GO AND SHARE IN THE COMMENTS*


### Thanks For Reading 
