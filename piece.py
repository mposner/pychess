# pychess
# mposner 11/11/14

from piece_attributes import *

class Piece:
	""" Represents a chess piece """
	
	def __init__(self, color, type):
		"""Initialize a new piece"""
		
		if isValidPieceType(type):
			self.type = type
		else:
			raise TypeError("Piece.__init__(): Invalid PieceType: " + type)
			
		if isValidColor(color):
			self.color = color
		else:
			raise TypeError("Piece.__init__(): Invalid piece Color: " + color)
			
	def __str__(self):
		return "[" + self.color[0] + "] " + self.type