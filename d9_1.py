data = open("d9.txt").read()

def decompress(code):
	i = 0
	while i < len(code):
		if code[i] == "(":

			close_parent_idx = code[i:].index(")")
			marker = code[i+1:i+close_parent_idx].split("x")

			copy_num_cha = int(marker[0])
			copy_times = int(marker[1]) - 1
			skip_marker = i + close_parent_idx + 1
			skip_decomp = i + copy_num_cha * copy_times

			# print('copy number of char', copy_num_cha)
			# print('copy x times', copy_times)
			# print('after the marker', code[skip_marker])
			# print("")

			code = code[:i] + code[skip_marker: skip_marker + copy_num_cha] * copy_times + code[skip_marker:]
			
			i = skip_decomp

		i += 1

	return code

result = decompress(data)

print(result)