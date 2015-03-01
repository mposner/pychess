# pychess
# mposner 11/11/14

from piece_attributes import *
from utils import isValidPosition

class Piece:
	""" Represents a chess piece """
	
	def __init__(self, color, type, position):
		"""Initialize a new piece"""
		
		if isValidPieceType(type):
			self.type = type
		else:
			raise TypeError("Piece.__init__(): Invalid PieceType: " + type)
			
		if isValidColor(color):
			self.color = color
		else:
			raise TypeError("Piece.__init__(): Invalid piece Color: " + color)
			
		if isValidPosition(position):
			self.position = position
		else:
			raise TypeError("Piece.__init__(): Invalid piece position: " + position)
			
			
	def __str__(self):
		return "[" + self.color[0] + "] " + self.type
	
	def shortstr(self):
	
		if(self.type == PieceType.KNIGHT):
			s = "N"
		else:
			s = self.type[0]
	
		if(self.color == Color.WHITE):
			return s
		else:
			return s.lower()
