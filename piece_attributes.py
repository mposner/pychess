# pychess
# mposner 11/11/14


class PieceType:
	""" Enum for the different possible types of pieces """
	
	KING="KING"
	QUEEN="QUEEN"
	BISHOP="BISHOP"
	KNIGHT="KNIGHT"
	ROOK="ROOK"
	PAWN="PAWN"

	
def isValidPieceType(type):
	""" Returns whether the given PieceType is valid """
	
	if type == PieceType.KING or type == PieceType.QUEEN or \
		type == PieceType.BISHOP or type == PieceType.KNIGHT or \
		type == PieceType.ROOK or type == PieceType.PAWN:
		return True
	else:
		return False
	
	
	
class Color:
	""" Enum for the two piece colors """
	
	WHITE="WHITE"
	BLACK="BLACK"

	
def isValidColor(color):
	""" Returns whether the given Color is valid """

	if color == Color.WHITE or color == Color.BLACK:
		return True
	else:
		return False
		