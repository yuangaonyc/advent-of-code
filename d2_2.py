txt = open("d2.txt").read()

answer = { '[-2, 0]' : 5,
	   '[-1, 0]' : 6,
	   '[0, 0]' : 7,
	   '[1, 0]' : 8,
	   '[2, 0]' : 9,
	   '[0, 1]' : 3,
	   '[-1, 1]' : 2,
	   '[1, 1]' : 4,
	   '[0, 2]' : 1,
	   '[0, -1]' : "B",
	   '[-1, -1]' : "A",
	   '[1, -1]' : "C",
	   '[0, -2]' : "D"
	 }

for line in txt.split("\n")[:-1]:
	me = [0,0]

	for letter in line:
		if letter == "L":
			move = me[:]
			move[0] -= 1
			if str(move) in answer.keys():
				me = move
			else:
				pass

		if letter == "R":
			move = me[:]
			move[0] += 1
			if str(move) in answer.keys():
				me = move
			else:
				pass
	
		if letter == "U":
			move = me[:]
			move[1] += 1
			if str(move) in answer.keys():
				me = move
			else:
				pass

		if letter == "D":
			move = me[:]
			move[1] -= 1
			if str(move) in answer.keys():
				me = move
			else:
				pass
	
	print(answer[str(me)])