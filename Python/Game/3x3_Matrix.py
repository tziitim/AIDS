import math
from settings import *

blank = 1;

Matrix = [[0 for x in range(SIZE)] for y in range(SIZE)];


def getWinner():#THIS FUNCTION IS INCOMPLETE!!!  We still need to fix over detection
    global Matrix
    global blank
    
    
    #total = sum(map(sum, Matrix))
    #total = total % SIZE
    #if total >= 4:
    #    return "TIED!" #Its a tie
    #if total % 2 == 1:
    #    return "O!";#X wins
    #if total % 2 == 0:
    #    return "Sadly, X...";#O Wins
    #return     10;#Game is not over.
    
    for j in range(0,SIZE):
        x = 1;
        o = 1;
        for k in range(0,SIZE):
            if Matrix[j][k] != 1:
                print("Matrix[" + str(j) + "]["+ str(k) + "] != X");
                x = 0
            if Matrix[j][k] != 2:
                print("Matrix[" + str(j) + "]["+ str(k) + "] != O");
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
    Matrix[int(xy % SIZE)][int((xy/SIZE))] = 1;

IsAIINIT = 0;

import AI;

def initAI():
    #__import__(AI);
    InitAI();
    IsAIINIT = 1;

def playertwo():
    global Matrix
    global blank
    #xy = max(min(int(input()),8),0);
    #
    #if istaken(xy):
    #    xy = max(min(int(input()),8),0);
    #    print("Please choose a different location on the board, as it is currently occupied.");
    #    playertwo();
    #    return
    #Matrix[int(xy % SIZE)][int((xy/SIZE))] = 2;
    AI.AIPlayerChoice(Matrix);


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
    #if isOver():
    winner = getWinner();
    if winner != -1:
        return winner;
    
    print("Your computer has succsesfully acquired AIDS");
    printboard();
    playerone();
    winner = getWinner();
    if winner != -1:
        return winner;
    printboard();
    playertwo();
    winner = getWinner();
    if winner != -1:
        return winner;
    #
    #Matrix[max(min(int(x),3),0)-1][max(min(int(y),3),0)-1] = 1;
    
    return tictactoe();
    
    
    
def printboard():
    #print("   1 2 3\n");
    #print(" 1 "+p(Matrix[0][0]) + "|" + p(Matrix[1][0]) + "|" + p(Matrix[2][0]));
    #print("   "+"-+-+-");
    #print(" 2 "+p(Matrix[0][1]) + "|" + p(Matrix[1][1]) + "|" + p(Matrix[2][1]));
    #print("   "+"-+-+-");
    #print(" 3 "+p(Matrix[0][2]) + "|" + p(Matrix[1][2]) + "|" + p(Matrix[2][2]));
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

