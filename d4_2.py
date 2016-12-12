txt = open("d4.txt").read()
data = txt.split("\n")

#################################
alphabet_id = {}
x=0
for i in 'abcdefghijklmnopqrstuvwxyz':
	alphabet_id[i] = x
	x += 1

def letter_to_id(letter):
	return alphabet_id[letter]

def id_to_letter(id):
	for l, i in alphabet_id.iteritems():
		if id == i:
			return(l)
#################################

sum = 0
counts = 0
for code in data[:-1]:
	copy = code[:]
	check = code[-6:-1]
	code = code[:-7]
	score = code.split('-')[-1]
	code = ''.join(code.split('-')[:-1])

	# decrypting
	def decrypt(code):
		code = list(code)
		for id, char in enumerate(code):
			code[id] = id_to_letter((letter_to_id(code[id]) + int(score)) % 26)
		code = ''.join(code)
		return code

	code = decrypt(code)

	# print(code)

	# counting word frequencies
	count_dict = {}
	for char in code:
		if char not in count_dict.keys():
			count_dict[char] = 1
		else:
			count_dict[char] += 1
	count_dict = sorted(sorted(count_dict.items(), key=lambda x: x[0]), key=lambda x: x[1], reverse=True)[:5]

	# checking and scoring
	against = ''
	for char_pair in count_dict:
		against += char_pair[0]

	# print(against, check)

	if check == against:
		counts += 1
		sum += int(score)

	# searching for north pole objects
	if 'north' in code:
		print(code, score)

print(counts)
print(sum)






