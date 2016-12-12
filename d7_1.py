txt = open("d7.txt").read()
data = txt.split("\n")
for id, row in enumerate(data):
	data[id] = data[id].replace("]","[").split("[")

def isTLS(string):
	i = 0
	while i <= len(string) - 4:
		if string[i] == string[i+3] and string[i+1] == string[i+2] and string[i] != string[i+1]:
			return True
		i += 1
	return False

for id_r, row in enumerate(data):
	for id_i, item in enumerate(data[id_r]):
		data[id_r][id_i] = isTLS(data[id_r][id_i])

result = [False] * len(data)
for id_r, row in enumerate(data):
	for id_i, item in enumerate(row):
		if id_i % 2 == 0 and item == True:
			result[id_r] = True
	for id_i, item in enumerate(row):
		if id_i % 2 != 0 and item == True:
			result[id_r] = False

print(result.count(True))