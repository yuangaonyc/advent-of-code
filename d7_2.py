txt = open("d7.txt").read()
data = txt.split("\n")
for id, row in enumerate(data):
	data[id] = data[id].replace("]","[").split("[")

for id_r, row in enumerate(data):
	data_transformed = [[],[]]
	for id_i, item in enumerate(row):
		if id_i % 2 == 0:
			data_transformed[0] += [item]
		else:
			data_transformed[1] += [item]
	data[id_r] = data_transformed

def isSSL(arr):
	arr_a = arr[0]
	arr_b = arr[1]
	all_strings_in_b = []
	for item in arr_b:
		i = 0
		while i <= len(item)-3:
			all_strings_in_b.append(item[i]+item[i+1]+item[i+2])
			i += 1

	for item in arr_a:
		i = 0
		while i <= len(item)-3:
			if item[i] == item[i+2] and item[i] != item[i+1]:
				look_for = item[i+1] + item[i] + item[i+1]
				if look_for in all_strings_in_b:
					return True
			i += 1

result = []
for row in data: 
	result.append(isSSL(row))

print(result.count(True))