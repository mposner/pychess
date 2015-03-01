# pychess
# mposner 2/28/15

import unittest
from board import *

class TestGetPiece(unittest.TestCase):

	def setUp(self):
		self.b = Board()
	
	def test_board_middle(self):
		self.assertIs(self.b.board[1][3], self.b.getPiece("D2"))

	def test_board_bot(self):
		self.assertIs(self.b.board[0][1], self.b.getPiece("B1"))

	def test_board_left(self):
		self.assertIs(self.b.board[2][0], self.b.getPiece("A3"))
		
	def test_board_right(self):
		self.assertIs(self.b.board[3][7], self.b.getPiece("H4"))

	def test_board_top(self):
		self.assertIs(self.b.board[7][5], self.b.getPiece("F8"))
		
	def test_board_outside_file(self):
		self.assertIsNone(self.b.getPiece("I7"))
		
	def test_board_outside_rank(self):
		self.assertIsNone(self.b.getPiece("D9"))
		
		
class TestValidMove(unittest.TestCase):	
	
	def setUp(self):
		self.b = Board()
	
	def test_pawn_up(self):
		self.assertTrue(self.b.isValidMove(self.b.getPiece("C2"), "C3"))
		
	def test_pawn_up2(self):
		self.assertTrue(self.b.isValidMove(self.b.getPiece("C2"), "C4"))
		
	def test_pawn_diag_up_left(self):
		self.assertFalse(self.b.isValidMove(self.b.getPiece("C2"), "D3"))
	
	def test_pawn_diag_up_right(self):
		self.assertFalse(self.b.isValidMove(self.b.getPiece("C2"), "B3"))
	
	def test_pawn_same(self):
		self.assertFalse(self.b.isValidMove(self.b.getPiece("C2"), "C2"))
	
	def test_pawn_down(self):
		self.assertFalse(self.b.isValidMove(self.b.getPiece("C2"), "C1"))
	
	def test_pawn_left(self):
		self.assertFalse(self.b.isValidMove(self.b.getPiece("C2"), "B2"))
	
	def test_pawn_diag_down_right(self):
		self.assertFalse(self.b.isValidMove(self.b.getPiece("C2"), "D1"))


if __name__ == '__main__':
	unittest.main(verbosity=2)		
