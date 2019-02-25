import math

blank = 1;

SIZE = 3;

Matrix = [[0 for x in range(3)] for y in range(3)];


def getWinner():#THIS FUNCTION IS INCOMPLETE!!!  We still need to fix over detection
    total = sum(map(sum, Matrix))
    total = total % SIZE
    if total >= 4:
        return "TIED!" #Its a tie
    if total % 2 == 1:
        return "O!";#X wins
    if total % 2 == 0:
        return "Sadly, X...";#O Wins
    return 	10;#Game is not over.



def istaken(pos):
    if Matrix[int(pos % SIZE)][int((pos/SIZE))] == 0:
        return 0;
    return 1;

def playerone():
    xy = max(min(int(input()),8),0);
    #x = input();
    #y = input();
    if istaken(xy):
        xy = max(min(int(input()),8),0);
	
    Matrix[int(xy % 3)][int((xy/3))] = 1;

def playertwo():
    xy = max(min(int(input()),8),0);
    #x = input();
    #y = input();
    if istaken(xy):
        xy = max(min(int(input()),8),0);
    Matrix[int(xy % SIZE)][int((xy/SIZE))] = 2;


def isOver():
    for i in range(SIZE):
        for j in range(SIZE):
            if Matrix[i][j] == 0:
                return 0;
    return 1;


def tictactoe():
    if isOver():
        winner = getWinner();
        
        return winner;
	
    print("Your computer has succsesfully acquired AIDS");
    printboard();
    playerone();
    printboard();
    playertwo();
    
    #
    #Matrix[max(min(int(x),3),0)-1][max(min(int(y),3),0)-1] = 1;
    
    return tictactoe();
    
    
    
def printboard():
	print("   1 2 3\n");
	print(" 1 "+p(Matrix[0][0]) + "|" + p(Matrix[1][0]) + "|" + p(Matrix[2][0]));
	print("   "+"-+-+-");
	print(" 2 "+p(Matrix[0][1]) + "|" + p(Matrix[1][1]) + "|" + p(Matrix[2][1]));
	print("   "+"-+-+-");
	print(" 3 "+p(Matrix[0][2]) + "|" + p(Matrix[1][2]) + "|" + p(Matrix[2][2]));

def p(i):
    if i == 0:
        return " ";
    if i == 1:
        return "X";
    if i == 2:
        return "O";
    return " ";
    
def main(args):
    winner = tictactoe();
    print("the winner is " + winner + "\n")
    return 0
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

