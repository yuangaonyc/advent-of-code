import hashlib

def computeMD5hash(string):
    m = hashlib.md5()
    m.update(string.encode('utf-8'))
    return m.hexdigest()

input = "cxdnnyjw"

i = 0
t = 0
while t < 8:
	i += 1
	hsh = computeMD5hash(input + str(i))
	if hsh[0:5] == "00000":
		print hsh[5]
		t += 1
