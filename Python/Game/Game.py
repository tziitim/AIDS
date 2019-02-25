import tensorflow as tf;

blank = 1;

Matrix = [[0 for x in range(3)] for y in range(3)];
												
def tictactoe():
    print("Your computer has succsesfully acquired AIDS");
    printboard();
    x = input();
    y = input();
    
    Matrix[max(min(int(x),3),0)-1][max(min(int(y),3),0)-1] = 1;
    
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



########################################################################
#
##-AI
#
########################################################################


def AI():
	
	
	print("[INFO]: Initalizing Placeholders...");
	tf.placeholder_with_default(0,tf.float32,name="g00");
	tf.placeholder_with_default(0,tf.float32,name="g01");
	tf.placeholder_with_default(0,tf.float32,name="g02");
	tf.placeholder_with_default(0,tf.float32,name="g10");
	tf.placeholder_with_default(0,tf.float32,name="g11");
	tf.placeholder_with_default(0,tf.float32,name="g12");
	tf.placeholder_with_default(0,tf.float32,name="g20");
	tf.placeholder_with_default(0,tf.float32,name="g21");
	tf.placeholder_with_default(0,tf.float32,name="g22");
	print(" Done.\n");
	
	print("[INFO]: Creating graph...");
	
	while 1==1:
		
		print("");







########################################################################


def main(args):
    tictactoe();
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
