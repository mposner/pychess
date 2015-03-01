# pychess
# mposner 11/23/14

from piece import Piece
from piece_attributes import PieceType, Color
from utils import isValidPosition

class Board:
	"""Represents a chess board"""
	
	def __init__(self):
		"""Initialize a new chess board"""
		
		self.makeNewPieces()
		
		
		
	def __str__(self):
		result = "   " + 33*"=" + "\n"
		
		for i in range(7,-1,-1):
			result += " " + str(i+1) + " | "
			
			for j in range(8):
				if self.board[i][j] is None:
					result += "  | "
				else:
					result += self.board[i][j].shortstr() + " | "
				
			result = result[:-1] + "\n"
			
			if i > 0:
				result += "   " + 33*"-" + "\n"
			else:
				result += "   " + 33*"=" + "\n"
				result += "     " + "   ".join(["A","B","C","D","E","F","G","H"])
		
		return result
		
	
	def getPiece(self, position):
		"""Return the piece at the given board square"""
		
		if not isValidPosition(position):
			return None
		
		rank = int(position[1]) - 1
		file = ord(position[0]) - ord("A")
		
		return self.board[rank][file]
	
	
	
	def isValidMove(self, piece, end):
		"""See if a move is valid for a given Piece"""
		
		if not isValidPosition(end):  #rule out bad position input
			return False
		
		startfile = ord(piece.position[0])  #file is column, A-H
		startrank = int(piece.position[1])  #rank is row, 1-8
		
		endfile = ord(end[0])
		endrank = int(end[1])
		
		filediff = abs(startfile - endfile)
		rankdiff = abs(startrank - endrank)
		
		if piece.type == PieceType.KING:
			if filediff <= 1 and rankdiff <= 1:
				return True
			else:
				return False
		
		elif piece.type == PieceType.QUEEN:
			if filediff == 0 or rankdiff == 0:
				return True
			elif filediff == rankdiff:
				return True
			else:
				return False
		
		elif piece.type == PieceType.BISHOP:
			if filediff == rankdiff:
				return True
			else:
				return False
				
		elif piece.type == PieceType.KNIGHT:
			if filediff == 0 and rankdiff == 0:
				return True
			elif filediff == 1 and rankdiff == 2:
				return True
			elif filediff == 2 and rankdiff == 1:
				return True
			else:
				return False
				
		elif piece.type == PieceType.ROOK:
			if filediff == 0 or rankdiff == 0:
				return True
			else:
				return False
		
		elif piece.type == PieceType.PAWN:
			
			if filediff == 0 and (endrank-startrank) == 1:
				# Normal move forward
				return True
			elif filediff == 1 and rankdiff == 1:
				# Only valid if taking an enemy piece
				if self.getPiece(end) is not None and \
				   self.getPiece(end).color != piece.color:
					return True
			elif filediff == 0 and (endrank-startrank) == 2:
				# Only valid if pawn is starting from starting position
				if int(piece.position[1]) == 2:
					return True			
			
			return False
		
		
		
	def makeNewPieces(self):
		"""Make a new set of pieces"""
		
		white = []
		
		white.append(Piece(Color.WHITE, PieceType.ROOK, "A1"))
		white.append(Piece(Color.WHITE, PieceType.KNIGHT, "B1"))
		white.append(Piece(Color.WHITE, PieceType.BISHOP, "C1"))
		white.append(Piece(Color.WHITE, PieceType.QUEEN, "D1"))
		white.append(Piece(Color.WHITE, PieceType.KING, "E1"))
		white.append(Piece(Color.WHITE, PieceType.BISHOP, "F1"))
		white.append(Piece(Color.WHITE, PieceType.KNIGHT, "G1"))
		white.append(Piece(Color.WHITE, PieceType.ROOK, "H1"))
		
		white.append(Piece(Color.WHITE, PieceType.PAWN, "A2"))
		white.append(Piece(Color.WHITE, PieceType.PAWN, "B2"))
		white.append(Piece(Color.WHITE, PieceType.PAWN, "C2"))
		white.append(Piece(Color.WHITE, PieceType.PAWN, "D2"))
		white.append(Piece(Color.WHITE, PieceType.PAWN, "E2"))
		white.append(Piece(Color.WHITE, PieceType.PAWN, "F2"))
		white.append(Piece(Color.WHITE, PieceType.PAWN, "G2"))
		white.append(Piece(Color.WHITE, PieceType.PAWN, "H2"))
		
		black = []
		
		black.append(Piece(Color.BLACK, PieceType.ROOK, "A8"))
		black.append(Piece(Color.BLACK, PieceType.KNIGHT, "B8"))
		black.append(Piece(Color.BLACK, PieceType.BISHOP, "C8"))
		black.append(Piece(Color.BLACK, PieceType.QUEEN, "D8"))
		black.append(Piece(Color.BLACK, PieceType.KING, "E8"))
		black.append(Piece(Color.BLACK, PieceType.BISHOP, "F8"))
		black.append(Piece(Color.BLACK, PieceType.KNIGHT, "G8"))
		black.append(Piece(Color.BLACK, PieceType.ROOK, "H8"))
		
		black.append(Piece(Color.BLACK, PieceType.PAWN, "A7"))
		black.append(Piece(Color.BLACK, PieceType.PAWN, "B7"))
		black.append(Piece(Color.BLACK, PieceType.PAWN, "C7"))
		black.append(Piece(Color.BLACK, PieceType.PAWN, "D7"))
		black.append(Piece(Color.BLACK, PieceType.PAWN, "E7"))
		black.append(Piece(Color.BLACK, PieceType.PAWN, "F7"))
		black.append(Piece(Color.BLACK, PieceType.PAWN, "G7"))
		black.append(Piece(Color.BLACK, PieceType.PAWN, "H7"))
		
		self.white = white
		self.black = black
		
		#2-D array representing the board (board[0] = rank 1)
		board = [[] for i in range(8)]
		
		board[0] = white[0:8]
		board[1] = white[8:]
		board[2] = [None for i in range(8)]
		board[3] = [None for i in range(8)]
		board[4] = [None for i in range(8)]
		board[5] = [None for i in range(8)]
		board[6] = black[8:]
		board[7] = black[0:8]
		
		self.board = board
