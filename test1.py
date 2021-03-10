# * This simple algorithim compares bytes and returns them(1 or 0)
# * if one of them is 1 then return 1
# * other than that return 0
# * EX: 1 ^ 0 = 1.......1 ^ 1 = 0.....0 ^ 0 = 0

# * more on 'exclusive or'/'xor' algorithim info here (https://en.wikipedia.org/wiki/Exclusive_or)

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



# * More on bytearray here (https://www.w3resource.com/python/python-bytes.php)
