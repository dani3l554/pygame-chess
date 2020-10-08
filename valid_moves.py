def check_valid(name,prev_pos,next_pos,board):
	if name == "":
		return False
	colour = name[0]
	if board[next_pos[1]][next_pos[0]] != "":
		if board[next_pos[1]][next_pos[0]][0] == colour:
			return False
	if name[1] == "r":
		if prev_pos[0] == next_pos[0] or prev_pos[1] == next_pos[1]:
			return True
		return False
	elif name[1] == "q":
		return True
	elif name[1] == "b":
		if prev_pos[0] - next_pos[0] == prev_pos[1] - next_pos[1] or prev_pos[0] + next_pos[0] == prev_pos[1] + next_pos[1]:
			return True
		return False
	elif name[1] == "n":
		if prev_pos[0] - next_pos[0] in (-2,-1,1,2):
			if prev_pos[0] - next_pos[0] == -2 or prev_pos[0] - next_pos[0] == 2:
				if prev_pos[1] - next_pos[1] in (1,-1):
					return True
			else:
				if prev_pos[1] - next_pos[1] in (2,-2):
					return True
			return False
