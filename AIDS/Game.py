#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Game.py
#  
#  Copyright 2019 Tim's Laptop <Tim's Laptop@LAPTOP-7R2QALN5>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  



blank = 1;



Matrix = [[0 for x in range(3)] for y in range(3)];
												

def tictactoe():
    print("Your computer has succsesfully acquired AIDS");
    printboard();
    x = input();
    y = input();
    
    Matrix[int(x)][int(y)] = 1;
    
    tictactoe();
    
    
    
def printboard():
	
	print(p(Matrix[0][0]) + "|" + p(Matrix[1][0]) + "|" + p(Matrix[2][0]));
	print("-+-+-");
	print(p(Matrix[0][1]) + "|" + p(Matrix[1][1]) + "|" + p(Matrix[2][1]));
	print("-+-+-");
	print(p(Matrix[0][2]) + "|" + p(Matrix[1][2]) + "|" + p(Matrix[2][2]));

def p(i):
    if i == 0:
        return " ";
    if i == 1:
        return "X";
    if i == 2:
        return "O";
    return " ";

def main(args):
    tictactoe();
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
