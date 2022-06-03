#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 18:51:50 2018

@author: yangmiao
"""

from checkers import Piece
import examples
from proj10 import apply_move

Piece.symbols = ['b', 'w']
Piece.symbols_king = ['B', 'W']

board = examples.board_figure1()
print("Figure 1 board:")
board.display()

errmsg = "Invalid move, please type 'hints' to get suggestions."
answer = "[[None, None, None, None, None, None, None, W], " \
    + "[None, None, W, None, W, None, None, None], " \
    + "[None, None, None, None, None, None, None, b], " \
    + "[w, None, w, None, b, None, b, None], " \
    + "[None, None, None, None, None, None, None, w], " \
    + "[w, None, w, None, b, None, b, None], " \
    + "[None, None, None, w, None, w, None, w], " \
    + "[w, None, None, None, None, None, None, None]]"
moves = [('c6', 'd5'), ('e4', 'f5'), ('e6', 'f7')]
for move in moves:
    try:
        apply_move(board, move)
    except Exception as err:
        print("Correct Exception message: \"{:s}\"".format(errmsg))
        print("Your Exception message: \"{:s}\"".format(str(err)))
        assert str(err) == errmsg
print("\nMoves applied:", moves)
board.display()
student = str(board.get_cells())
print("Correct board state:", answer)
print("Your board state:", student)
assert student == answer

print("\nFigure 1 board after black moves:")
board.display()
answer = "[[None, W, None, W, None, None, None, None], " \
    + "[None, None, None, None, None, None, W, None], " \
    + "[None, w, None, None, None, None, None, b], " \
    + "[None, None, w, None, b, None, b, None], " \
    + "[None, w, None, None, None, None, None, w], " \
    + "[None, None, w, None, b, None, b, None], " \
    + "[None, w, None, w, None, w, None, w], " \
    + "[None, None, None, None, None, None, None, None]]"
moves = [('a8', 'b7'), ('b3', 'a2'), ('b5', 'a4'), ('d1', 'c2'), \
         ('f1', 'e2'), ('h1', 'g2')]
for move in moves:
    try:
        print("applying move:", move)
        apply_move(board, move)
    except Exception as err:
        print("Correct Exception message: \"{:s}\"".format(errmsg))
        print("Your Exception message: \"{:s}\"".format(str(err)))
        assert str(err) == errmsg
print("\nMoves applied:", moves)
board.display()
student = str(board.get_cells())
print("Correct board state:", answer)
print("Your board state:", student, "\n")
