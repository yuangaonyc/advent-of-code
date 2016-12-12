import hashlib

def computeMD5hash(string):
    m = hashlib.md5()
    m.update(string.encode('utf-8'))
    return m.hexdigest()

input = "cxdnnyjw"

password = [None, None, None, None, None, None, None, None]

i = 0
while None in password:
	i += 1
	hsh = computeMD5hash(input + str(i))
	if hsh[0:5] == "00000":
		print("found 5 zeros and the 6th char is " + hsh[5])
		try: 
			new_input_id = int(hsh[5])
			if new_input_id < 8:
				print("and it can be used in the password")
				if password[new_input_id] == None:
					password[new_input_id] = hsh[6]
					print('I got one!')
					print(password)
		except:
			pass