me = [0,0]
dir = 'n'

input = 'L1, L5, R1, R3, L4, L5, R5, R1, L2, L2, L3, R4, L2, R3, R1, L2, R5, R3, L4, R4, L3, R3, R3, L2, R1, L3, R2, L1, R4, L2, R4, L4, R5, L3, R1, R1, L1, L3, L2, R1, R3, R2, L1, R4, L4, R2, L189, L4, R5, R3, L1, R47, R4, R1, R3, L3, L3, L2, R70, L1, R4, R185, R5, L4, L5, R4, L1, L4, R5, L3, R2, R3, L5, L3, R5, L1, R5, L4, R1, R2, L2, L5, L2, R4, L3, R5, R1, L5, L4, L3, R4, L3, L4, L1, L5, L5, R5, L5, L2, L1, L2, L4, L1, L2, R3, R1, R1, L2, L5, R2, L3, L5, L4, L2, L1, L2, R3, L1, L4, R3, R3, L2, R5, L1, L3, L3, L3, L5, R5, R1, R2, L3, L2, R4, R1, R1, R3, R4, R3, L3, R3, L5, R2, L2, R4, R5, L4, L3, L1, L5, L1, R1, R2, L1, R3, R4, R5, R2, R3, L2, L1, L5'
map = input.split(", ")

for move in map:
	turn = move[0]
	steps = int(move[1:])

	if dir == 'n':
		if turn == 'L':
			me[0] = me[0] - steps
			dir = 'w'
		elif turn == 'R':
			me[0] = me[0] + steps
			dir = 'e'
	elif dir == 'e':
		if turn == 'L':
			me[1] = me[1] + steps
			dir = 'n'
		elif turn == 'R':
			me[1] = me[1] - steps
			dir = 's'
	elif dir == 's':
		if turn == 'L':
			me[0] += steps
			dir = 'e'
		elif turn == 'R':
			me[0] = me[0] - steps
			dir ='w'
	elif dir == 'w':
		if turn == 'L':
			me[1] = me[1] - steps
			dir = 's'
		elif turn == 'R':
			me[1] = me[1] + steps
			dir = 'n'

print(me)