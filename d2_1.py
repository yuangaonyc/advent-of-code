txt = open("d2.txt").read()

for line in txt.split("\n")[:-1]:
	me = [0,0]
	for letter in line:
		if letter == "L":
			if me[0] == -1:
				pass
			else:
				me[0] -= 1

		if letter == "R":
			if me[0] == 1:
				pass
			else:
				me[0] += 1
	
		if letter == "U":
			if me[1] == 1:
				pass
			else:
				me[1] += 1

		if letter == "D":
			if me[1] == -1:
				pass
			else:
				me[1] -= 1
	
	answer = { '[0, 0]' : 5,
			   '[1, 0]' : 6,
			   '[-1, 0]' : 4,
			   '[0, 1]' : 2,
			   '[-1, 1]' : 1,
			   '[1, 1]' : 3,
			   '[0, -1]' : 8,
			   '[-1, -1]' : 7,
			   '[1, -1]' : 9
			 }
	print(answer[str(me)])