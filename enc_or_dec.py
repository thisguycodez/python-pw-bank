


# encrypt or decrypt
def enc_n_dec_toggle(key):	
	# open the file in read mode as bytes
	f = open('./data/word-bank','rb')
	# save it to var
	content = f.read()
	f.close()



	# change content into an array of given bytes
	content = bytearray(content)


	# loop through content with enumerate to get i
	for i,cur_val in enumerate(content):
		# value needs to stay between 1-255

		# ^ sets each (cur_val ^ key) to 1 if one of them is 1, else 0
		content[i] = cur_val ^ key

		f = open('./data/word-bank', 'wb')
		f.write(content)
		f.close()




enc_n_dec_toggle(222)
