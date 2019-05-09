import math
from settings import *

blank = 1;

Matrix = [[0 for x in range(SIZE)] for y in range(SIZE)];


def getWinner():
    global Matrix
    global blank
    
    for j in range(0,SIZE):
        x = 1;
        o = 1;
        for k in range(0,SIZE):
            if Matrix[j][k] != 1:
                x = 0
            if Matrix[j][k] != 2:
                o = 0
        if o == 1:
            return 'O';
        if x == 1:
            return 'X'
            
    fx = 1;
    fo = 1;    
    for j in range(0,SIZE):
        if Matrix[j][j] != 1:
            fx = 0;
        if Matrix[j][j] != 2:
            fo = 0;
    if fx == 1:
        return 'X';
    if fo == 1:
        return 'O'; 
    fx = 1;
    fo = 1;
    for j in range(0,SIZE):
        if Matrix[SIZE-1-j][SIZE-1-j] != 1:
            fx = 0;
        if Matrix[SIZE-1-j][SIZE-1-j] != 2:
            fo = 0;
    if fx == 1:
        return 'X';
    if fo == 1:
        return 'O'; 
    return -1;
    



def istaken(pos):
    global Matrix
    global blank
    if Matrix[int(pos % SIZE)][int((pos/SIZE))] == 0:
        return 0;
    return 1;

def playerone():
    global Matrix
    global blank
    xy = max(min(int(input()),8),0);
		
    if istaken(xy):
        xy = max(min(int(input()),8),0);
        print("Please choose a different location on the board, as it is currently occupied.");
        playerone();
        return
    Matrix[int(xy % SIZE)][int((xy/SIZE))] = 2;

IsAIINIT = 0;

import AI;

def initAI():
    InitAI();


def playertwo():
    global Matrix
    global blank
    choice = AI.AIPlayerChoice(Matrix);
    print("AI choose " + str(choice));
    
    if istaken(choice):
        playertwo();
        return
    
    
    Matrix[int(choice % SIZE)][int((choice/SIZE))] = 1;

def isOver():
    for i in range(SIZE):
        for j in range(SIZE):
            if Matrix[i][j] == 0:
                return 0;
    for i in range(SIZE):
        if Matrix[i][i] == 0:
                return 0;
    return 1;


def tictactoe():
    
    
    
    winner = getWinner();
    if winner != -1:
        return winner;
    
    printboard();
    playerone();
    playertwo();
    return tictactoe();
    
    
    
def printboard():
    for j in range(0,SIZE):
        print("");
        for k in range(0,SIZE):
            print(p(Matrix[k][j],j,k),end = "");    
    print("\n");	
    

def p(i,j,k):
    if i == 0:
        return  str((j*SIZE)+k);
    if i == 1:
        return "X";
    if i == 2:
        return "O";
    return " ";
    
def main(args):
    AI.InitAI();
    winner = tictactoe();
    printboard();
    print("the winner is " + winner + "\n")
    return 0
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

