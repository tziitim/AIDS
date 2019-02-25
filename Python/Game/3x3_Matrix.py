import math

blank = 1;

Matrix = [[0 for x in range(3)] for y in range(3)];

def istaken(pos):
    if Matrix[int(pos % 3)][int((pos/3))] == 0:
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
    Matrix[int(xy % 3)][int((xy/3))] = 2;							
def tictactoe():
    print("Your computer has succsesfully acquired AIDS");
    printboard();
    playerone();
    printboard();
    playertwo();
    #
    #Matrix[max(min(int(x),3),0)-1][max(min(int(y),3),0)-1] = 1;
    
    tictactoe();
    
    
    
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
    tictactoe();
    return 0
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

