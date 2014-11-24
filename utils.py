# pychess
# mposner 11/23/14


def isValidPosition(position):
		"""Determines whether the given position is valid (A-H, 1-8)"""
		if position[0].lower() >= "a" and position[0].lower() <= "h" \
			and position[1] >= "1" and position[1] <= "8":
			return True
		else:
			return False
	