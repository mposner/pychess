# pychess
# mposner 11/23/14


def isValidPosition(position):
		"""Determines whether the given position is valid (A-H, 1-8)"""
		if position[0].upper() >= "A" and position[0].upper() <= "H" \
			and position[1] >= "1" and position[1] <= "8":
			return True
		else:
			return False
	