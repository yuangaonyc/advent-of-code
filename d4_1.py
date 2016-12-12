txt = open("d4.txt").read()
data = txt.split("\n")

sum = 0
counts = 0
for code in data[:-1]:
	copy = code[:]
	check = code[-6:-1]
	code = code[:-7]
	score = code.split('-')[-1]
	code = ''.join(code.split('-')[:-1])

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

	if check == against:
		counts += 1
		sum += int(score)

print(counts)
print(sum)